// DOM Elements
const url = document.querySelector('#url');
const format = document.querySelector('#format');
const title = document.querySelector('#title');
const form = document.querySelector('#download_form');

const loader = document.getElementById('load');
const container = document.querySelector('.container');

// Functions for the loading circle
function showLoadingSpinner() {
	container.style.display = 'none';
	loader.classList.add('loader');
}
  
function removeLoadingSpinner() {
	container.style.display = 'block';
	loader.classList.remove('loader');
} 

// Listen for a click on the download button
form.addEventListener('submit', (e) => {
    e.preventDefault();
    downloadVideo();
});

async function downloadVideo() {
    if (url.value == '' || format.value == '' || title.value == '') {
        location.href = '/error';
        return;
    }
    // Download the video
    showLoadingSpinner();
    await fetch(`/download?url=${url.value}&format=${format.value}`)
        .then(response => response.blob())
        .then(file => {
        // Create a temporary anchor element
        const a = document.createElement('a');

        // Set the href and download attributes of the anchor element
        let tempUrl = URL.createObjectURL(file);
        a.href = tempUrl;
        a.download = `${title.value}.${format.value}`;

        // Add the element to the DOM
        document.body.appendChild(a);

        // Click the anchor element to trigger the download
        a.click();

        // Clean up
        URL.revokeObjectURL(tempUrl);
        a.remove()
        url.value = '';
        title.value = '';
        format.value = '';
    });
    removeLoadingSpinner();
}

