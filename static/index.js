// // DOM Elements
// const video_id = document.querySelector('#url');
// const format = document.querySelector('#format');
// const form = document.querySelector('#download_form');

// // Listen for a click on the download button
// downloadBtn.addEventListener('submit', downloadVideo())

// function downloadVideo(e) {
//     e.preventDefault();

//     // Download the video
//     fetch(`/download?url=https://www.youtube.com/watch?v=${video_id}`)
//         .then(response => {
//         // Create a temporary anchor element
//         const a = document.createElement('a');
//         a.style.display = 'none';
//         document.body.appendChild(a);

//         // Set the href and download attributes of the anchor element
//         a.href = window.URL.createObjectURL(response.blob());
//         a.download = 'video.mp4';

//         // Click the anchor element to trigger the download
//         a.click();

//         // Clean up
//         window.URL.revokeObjectURL(a.href);
//         document.body.removeChild(a);
//         });
// }

