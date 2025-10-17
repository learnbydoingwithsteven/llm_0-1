// Course 001: Introduction to Language Models - Interactive Script

let modelResults = [];

// Event listeners
document.getElementById('trainBtn').addEventListener('click', trainModels);

// Tab switching for probability visualization
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        const n = parseInt(e.target.dataset.n);
        showProbabilityChart(n);
    });
});

async function trainModels() {
    const text = document.getElementById('trainText').value.trim();
    
    if (!text) {
        alert('Please enter some training text!');
        return;
    }
    
    // Get selected n-gram orders
    const nValues = [];
    if (document.getElementById('n1').checked) nValues.push(1);
    if (document.getElementById('n2').checked) nValues.push(2);
    if (document.getElementById('n3').checked) nValues.push(3);
    
    if (nValues.length === 0) {
        alert('Please select at least one n-gram order!');
        return;
    }
    
    // Show loading
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    
    try {
        const response = await fetch('/api/train', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                n_values: nValues
            })
        });
        
        modelResults = await response.json();
        
        // Hide loading, show results
        document.getElementById('loading').style.display = 'none';
        document.getElementById('results').style.display = 'block';
        
        // Display all results
        displayMetrics();
        displayPerplexityChart();
        displayProbabilityChart(nValues[0]);
        displayGeneratedTexts();
        displayModelDetails();
        
    } catch (error) {
        console.error('Error:', error);
        alert('Error training models. Please try again.');
        document.getElementById('loading').style.display = 'none';
    }
}

function displayMetrics() {
    const container = document.getElementById('metricsCards');
    container.innerHTML = '';
    
    const colors = {1: '#ff6b6b', 2: '#4ecdc4', 3: '#45b7d1'};
    const names = {1: 'Unigram', 2: 'Bigram', 3: 'Trigram'};
    
    modelResults.forEach(result => {
        const card = document.createElement('div');
        card.className = `metric-card n${result.n}`;
        card.innerHTML = `
            <h3>${names[result.n]} Model</h3>
            <div class="metric-item">
                <span class="metric-label">Perplexity:</span>
                <span class="metric-value">${result.perplexity.toFixed(2)}</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Vocabulary Size:</span>
                <span class="metric-value">${result.vocab_size}</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">Contexts:</span>
                <span class="metric-value">${result.num_contexts}</span>
            </div>
            <div class="metric-item">
                <span class="metric-label">N-gram Order:</span>
                <span class="metric-value">${result.n}</span>
            </div>
        `;
        container.appendChild(card);
    });
}

function displayPerplexityChart() {
    const names = {1: 'Unigram', 2: 'Bigram', 3: 'Trigram'};
    const colors = {1: '#ff6b6b', 2: '#4ecdc4', 3: '#45b7d1'};
    
    const trace = {
        x: modelResults.map(r => names[r.n]),
        y: modelResults.map(r => r.perplexity),
        type: 'bar',
        marker: {
            color: modelResults.map(r => colors[r.n]),
            line: {
                color: '#333',
                width: 2
            }
        },
        text: modelResults.map(r => r.perplexity.toFixed(2)),
        textposition: 'outside',
        textfont: {
            size: 14,
            weight: 'bold'
        }
    };
    
    const layout = {
        title: {
            text: 'Perplexity by Model (Lower is Better)',
            font: { size: 18, weight: 'bold' }
        },
        xaxis: {
            title: 'Model Type',
            titlefont: { size: 14 }
        },
        yaxis: {
            title: 'Perplexity',
            titlefont: { size: 14 }
        },
        plot_bgcolor: '#f8f9fa',
        paper_bgcolor: 'white',
        margin: { t: 60, b: 60, l: 60, r: 40 }
    };
    
    Plotly.newPlot('perplexityChart', [trace], layout, {responsive: true});
}

function displayProbabilityChart(n) {
    const result = modelResults.find(r => r.n === n);
    if (!result) return;
    
    const names = {1: 'Unigram', 2: 'Bigram', 3: 'Trigram'};
    const colors = {1: '#ff6b6b', 2: '#4ecdc4', 3: '#45b7d1'};
    
    // Get first context with predictions
    const contexts = Object.keys(result.top_predictions);
    if (contexts.length === 0) return;
    
    const traces = [];
    
    contexts.slice(0, 3).forEach((context, idx) => {
        const predictions = result.top_predictions[context];
        const trace = {
            x: predictions.map(p => p.word),
            y: predictions.map(p => p.prob),
            type: 'bar',
            name: `Context: "${context}"`,
            marker: {
                color: colors[n],
                opacity: 1 - (idx * 0.2)
            }
        };
        traces.push(trace);
    });
    
    const layout = {
        title: {
            text: `${names[n]} Probability Distribution`,
            font: { size: 18, weight: 'bold' }
        },
        xaxis: {
            title: 'Next Word',
            titlefont: { size: 14 }
        },
        yaxis: {
            title: 'Probability',
            titlefont: { size: 14 },
            range: [0, 1]
        },
        barmode: 'group',
        plot_bgcolor: '#f8f9fa',
        paper_bgcolor: 'white',
        margin: { t: 60, b: 80, l: 60, r: 40 },
        legend: {
            orientation: 'h',
            y: -0.2
        }
    };
    
    Plotly.newPlot('probabilityChart', traces, layout, {responsive: true});
}

function showProbabilityChart(n) {
    displayProbabilityChart(n);
}

function displayGeneratedTexts() {
    const container = document.getElementById('generatedTexts');
    container.innerHTML = '';
    
    const names = {1: 'Unigram', 2: 'Bigram', 3: 'Trigram'};
    
    modelResults.forEach(result => {
        const div = document.createElement('div');
        div.className = `generated-text n${result.n}`;
        div.innerHTML = `
            <h4>🎲 ${names[result.n]} Generated Text</h4>
            <p>"${result.sample}"</p>
        `;
        container.appendChild(div);
    });
}

function displayModelDetails() {
    const container = document.getElementById('modelDetails');
    container.innerHTML = '';
    
    const names = {1: 'Unigram', 2: 'Bigram', 3: 'Trigram'};
    
    modelResults.forEach(result => {
        const contexts = Object.keys(result.top_predictions);
        if (contexts.length === 0) return;
        
        const card = document.createElement('div');
        card.className = 'detail-card';
        
        let predictionsHTML = '';
        contexts.slice(0, 2).forEach(context => {
            const predictions = result.top_predictions[context].slice(0, 5);
            predictionsHTML += `
                <div style="margin-bottom: 20px;">
                    <strong>Context: "${context}"</strong>
                    <div class="prediction-list" style="margin-top: 10px;">
                        ${predictions.map(p => `
                            <div class="prediction-item">
                                <span class="prediction-word">${p.word}</span>
                                <div class="prediction-bar" style="width: ${p.prob * 100}%"></div>
                                <span class="prediction-prob">${(p.prob * 100).toFixed(1)}%</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        });
        
        card.innerHTML = `
            <h4>${names[result.n]} Model - Top Predictions</h4>
            ${predictionsHTML}
        `;
        
        container.appendChild(card);
    });
}

// Initialize with sample text
window.addEventListener('load', () => {
    console.log('Course 001: Introduction to Language Models loaded');
});
