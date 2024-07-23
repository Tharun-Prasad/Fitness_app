function includeHTML() {
    const includeElements = document.querySelectorAll('[data-include-html]');
    includeElements.forEach(el => {
        const file = el.getAttribute('data-include-html');
        if (file) {
            fetch(file)
                .then(response => response.text())
                .then(data => {
                    el.innerHTML = data;
                    el.removeAttribute('data-include-html');
                })
                .catch(err => {
                    console.error(`Error loading file ${file}:`, err);
                    el.innerHTML = "Content not found.";
                });
        }
    });
}

document.addEventListener("DOMContentLoaded", includeHTML);
