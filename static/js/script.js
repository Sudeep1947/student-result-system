document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeBtn = document.getElementById('theme-toggle');
    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            const isDark = document.body.classList.contains('dark-mode');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        });
    }

    // Load Theme
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
    }

    // Search and Filter
    const searchInput = document.getElementById('searchInput');
    const gradeFilter = document.getElementById('gradeFilter');
    const tableRows = document.querySelectorAll('#resultsTable tbody tr');

    function filterTable() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedGrade = gradeFilter.value;

        tableRows.forEach(row => {
            const text = row.textContent.toLowerCase();
            const grade = row.getAttribute('data-grade');
            const matchesSearch = text.includes(searchTerm);
            const matchesGrade = !selectedGrade || grade === selectedGrade;

            row.style.display = matchesSearch && matchesGrade ? '' : 'none';
        });
    }

    if (searchInput) searchInput.addEventListener('input', filterTable);
    if (gradeFilter) gradeFilter.addEventListener('change', filterTable);

    // Charts
    if (typeof gradeData !== 'undefined') {
        const ctxGrade = document.getElementById('gradeChart').getContext('2d');
        new Chart(ctxGrade, {
            type: 'doughnut',
            data: {
                labels: Object.keys(gradeData),
                datasets: [{
                    data: Object.values(gradeData),
                    backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b']
                }]
            },
            options: { maintainAspectRatio: false }
        });

        const ctxPerf = document.getElementById('performanceChart').getContext('2d');
        new Chart(ctxPerf, {
            type: 'bar',
            data: {
                labels: studentNames,
                datasets: [{
                    label: 'Total Marks',
                    data: studentMarks,
                    backgroundColor: 'rgba(78, 115, 223, 0.5)',
                    borderColor: 'rgba(78, 115, 223, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: { y: { beginAtZero: true } },
                maintainAspectRatio: false
            }
        });
    }
});
