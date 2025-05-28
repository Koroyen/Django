document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('input[name="q"]');
    const container = document.getElementById('hotspot-list-container');
    let timeout = null;

    if (searchInput && container) {
        // Prevent form submit
        searchInput.form && searchInput.form.addEventListener('submit', function(e) {
            e.preventDefault();
        });

        searchInput.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(function() {
                const query = searchInput.value;
                fetch(`?q=${encodeURIComponent(query)}`, {
                    headers: {
                        'x-requested-with': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    container.innerHTML = data.html;
                });
            }, 300);
        });
    }
});