from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/download')
def download():
  # Get the URL of the YouTube video
  url = request.args.get('url')
  format = request.args.get('format')
  
  yt = YouTube(url)
  if format == 'mp4':
    # Download the video
    video = yt.streams.get_highest_resolution()
    file_path = video.download('/YouTube Downloads')
  elif format == 'mp3':
    mp3_stream = yt.streams.get_audio_only()
    file_path = mp3_stream.download('/YouTube Downloads')

  # Send the file to the browser
  return send_file(file_path, as_attachment=True)

@app.route('/error')
def error():
    return render_template('error.html', message='Please fill in all fields!')