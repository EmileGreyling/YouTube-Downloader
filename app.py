from flask import Flask, render_template, request, redirect, send_file, url_for
from pytube import YouTube

# Flask app
app = Flask(__name__)


# Main site
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', video="False")

# Route to download the video
@app.route('/download', methods=['POST'])
def download():
    # Get the URL of the video to download
    video_id = request.form.get('video_id')
    format = request.form.get('format')

    if not format or not video_id:
        return render_template('error.html', message = 'Please fill in all fields!')

    # Download the video
    file_path = '/YouTube Downloads'
    downloadVideoMp4(video_id, file_path)
    
    # Send the video to the browser as a response
    return render_template('index.html', form_submitted=True, message=f'Your file was saved at {file_path}')


def downloadVideoMp4(video_id, file_path):
    # Get the video stream and return it
    yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
    video = yt.streams.get_highest_resolution()
    video = video.download(file_path)
