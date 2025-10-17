// Navigation and interaction logic for the course catalog

let currentFilter = 'all';
let completedCourses = new Set(JSON.parse(localStorage.getItem('completedCourses') || '[]'));

// Initialize the page
document.addEventListener('DOMContentLoaded', () => {
    renderCourses();
    setupEventListeners();
    updateProgress();
});

function setupEventListeners() {
    // Search functionality
    document.getElementById('searchBox').addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        filterCourses(searchTerm);
    });

    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            currentFilter = e.target.dataset.module;
            renderCourses();
        });
    });
}

function renderCourses() {
    const container = document.getElementById('modulesContainer');
    container.innerHTML = '';

    // Group courses by module
    const coursesByModule = {};
    COURSES_DATA.forEach(course => {
        if (!coursesByModule[course.module]) {
            coursesByModule[course.module] = [];
        }
        coursesByModule[course.module].push(course);
    });

    // Render each module
    Object.keys(coursesByModule).sort((a, b) => parseInt(a) - parseInt(b)).forEach(moduleNum => {
        if (currentFilter !== 'all' && currentFilter !== moduleNum) {
            return;
        }

        const module = document.createElement('div');
        module.className = 'module';
        module.id = `module-${moduleNum}`;

        const moduleHeader = document.createElement('div');
        moduleHeader.className = 'module-header';
        moduleHeader.innerHTML = `
            <div class="module-title">📚 Module ${moduleNum}: ${MODULE_NAMES[moduleNum]}</div>
            <div class="module-count">${coursesByModule[moduleNum].length} courses</div>
        `;

        const coursesGrid = document.createElement('div');
        coursesGrid.className = 'courses-grid';

        coursesByModule[moduleNum].forEach(course => {
            const card = createCourseCard(course);
            coursesGrid.appendChild(card);
        });

        module.appendChild(moduleHeader);
        module.appendChild(coursesGrid);
        container.appendChild(module);

        // Toggle module visibility
        moduleHeader.addEventListener('click', () => {
            coursesGrid.style.display = coursesGrid.style.display === 'none' ? 'grid' : 'none';
        });
    });
}

function createCourseCard(course) {
    const card = document.createElement('div');
    card.className = `course-card module-${course.module}`;
    
    const isCompleted = completedCourses.has(course.id);
    
    card.innerHTML = `
        <div class="course-number">Course ${course.id} ${isCompleted ? '✅' : ''}</div>
        <div class="course-title">${course.title}</div>
        <p style="color: #666; font-size: 0.95em; line-height: 1.5;">${course.description}</p>
        <div class="course-features">
            <span class="feature-tag">📊 Metrics</span>
            <span class="feature-tag">📈 Visualizations</span>
            <span class="feature-tag">💻 Interactive</span>
        </div>
        <button class="launch-btn" onclick="launchCourse('${course.id}', '${course.name}')">
            🚀 Launch Course
        </button>
    `;

    // Mark as completed on click
    card.addEventListener('dblclick', () => {
        toggleCourseCompletion(course.id);
        renderCourses();
        updateProgress();
    });

    return card;
}

function launchCourse(id, name) {
    const courseDir = `course_${id}_${name}`;
    window.open(`${courseDir}/index.html`, '_blank');
}

function toggleCourseCompletion(courseId) {
    if (completedCourses.has(courseId)) {
        completedCourses.delete(courseId);
    } else {
        completedCourses.add(courseId);
    }
    localStorage.setItem('completedCourses', JSON.stringify([...completedCourses]));
}

function updateProgress() {
    const completed = completedCourses.size;
    const total = COURSES_DATA.length;
    const percentage = (completed / total * 100).toFixed(1);
    
    document.getElementById('progressFill').style.width = `${percentage}%`;
    document.getElementById('progressFill').textContent = `${percentage}%`;
    document.getElementById('completedCount').textContent = completed;
}

function filterCourses(searchTerm) {
    if (!searchTerm) {
        document.querySelectorAll('.course-card').forEach(card => {
            card.style.display = 'block';
        });
        return;
    }

    document.querySelectorAll('.course-card').forEach(card => {
        const title = card.querySelector('.course-title').textContent.toLowerCase();
        const description = card.querySelector('p').textContent.toLowerCase();
        
        if (title.includes(searchTerm) || description.includes(searchTerm)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        document.getElementById('searchBox').focus();
    }
    
    // Escape to clear search
    if (e.key === 'Escape') {
        document.getElementById('searchBox').value = '';
        filterCourses('');
    }
});

// Export progress
function exportProgress() {
    const data = {
        completed: [...completedCourses],
        total: COURSES_DATA.length,
        percentage: (completedCourses.size / COURSES_DATA.length * 100).toFixed(1),
        timestamp: new Date().toISOString()
    };
    
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'llm-courses-progress.json';
    a.click();
}

// Add export button functionality
console.log('💡 Tip: Double-click a course card to mark it as completed!');
console.log('💡 Tip: Use Ctrl/Cmd + K to quickly search courses');
console.log('💡 Tip: Call exportProgress() in console to download your progress');
