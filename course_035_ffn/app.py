"""
Course 001: Introduction to Language Models
Interactive application with visualization and metrics
"""

import http.server
import socketserver
import webbrowser
import threading
import json
from collections import defaultdict, Counter
import math
import random

class LanguageModel:
    """Base class for language models"""
    def __init__(self, n=1):
        self.n = n
        self.vocab = set()
        self.counts = defaultdict(lambda: defaultdict(int))
        self.context_counts = defaultdict(int)
        
    def train(self, text):
        """Train the n-gram model"""
        tokens = text.lower().split()
        self.vocab.update(tokens)
        
        # Add start/end tokens
        tokens = ['<START>'] * (self.n - 1) + tokens + ['<END>']
        
        # Count n-grams
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i+self.n-1]) if self.n > 1 else ()
            word = tokens[i+self.n-1]
            self.counts[context][word] += 1
            self.context_counts[context] += 1
    
    def probability(self, word, context=()):
        """Calculate P(word|context)"""
        if self.context_counts[context] == 0:
            return 1.0 / len(self.vocab)  # Uniform distribution for unseen context
        return self.counts[context][word] / self.context_counts[context]
    
    def perplexity(self, text):
        """Calculate perplexity on test text"""
        tokens = text.lower().split()
        tokens = ['<START>'] * (self.n - 1) + tokens + ['<END>']
        
        log_prob = 0
        count = 0
        
        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i+self.n-1]) if self.n > 1 else ()
            word = tokens[i+self.n-1]
            prob = self.probability(word, context)
            if prob > 0:
                log_prob += math.log(prob)
                count += 1
        
        if count == 0:
            return float('inf')
        
        return math.exp(-log_prob / count)
    
    def generate(self, num_words=20, temperature=1.0):
        """Generate text using the model"""
        if self.n == 1:
            context = ()
        else:
            context = tuple(['<START>'] * (self.n - 1))
        
        generated = []
        
        for _ in range(num_words):
            if context not in self.counts or len(self.counts[context]) == 0:
                break
            
            # Get probability distribution
            words = list(self.counts[context].keys())
            probs = [self.counts[context][w] / self.context_counts[context] for w in words]
            
            # Apply temperature
            if temperature != 1.0:
                probs = [p ** (1.0 / temperature) for p in probs]
                total = sum(probs)
                probs = [p / total for p in probs]
            
            # Sample next word
            word = random.choices(words, weights=probs)[0]
            
            if word == '<END>':
                break
            
            generated.append(word)
            
            # Update context
            if self.n > 1:
                context = tuple(list(context[1:]) + [word])
        
        return ' '.join(generated)

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler for API endpoints"""
    
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        if self.path == '/api/train':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            train_text = data.get('text', '')
            n_values = data.get('n_values', [1, 2, 3])
            
            results = []
            
            for n in n_values:
                model = LanguageModel(n=n)
                model.train(train_text)
                
                # Calculate metrics
                perplexity = model.perplexity(train_text)
                vocab_size = len(model.vocab)
                
                # Generate sample text
                sample = model.generate(num_words=20, temperature=1.0)
                
                # Get top predictions for visualization
                top_predictions = {}
                for context, words in list(model.counts.items())[:5]:
                    context_str = ' '.join(context) if context else '<START>'
                    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]
                    top_predictions[context_str] = [
                        {'word': w, 'prob': c / model.context_counts[context]}
                        for w, c in sorted_words
                    ]
                
                results.append({
                    'n': n,
                    'perplexity': perplexity,
                    'vocab_size': vocab_size,
                    'sample': sample,
                    'top_predictions': top_predictions,
                    'num_contexts': len(model.counts)
                })
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(results).encode())
        else:
            self.send_response(404)
            self.end_headers()

def start_server(port=8000):
    """Start the HTTP server"""
    handler = RequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server running at http://localhost:{port}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()

if __name__ == '__main__':
    PORT = 8000
    
    # Open browser after short delay
    def open_browser():
        import time
        time.sleep(1)
        webbrowser.open(f'http://localhost:{PORT}')
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Start server
    start_server(PORT)
