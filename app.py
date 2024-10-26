from flask import Flask, render_template, request, send_file
from pytubefix import YouTube
import io

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
    file_stream = io.BytesIO()
    video.stream_to_buffer(file_stream)
    file_stream.seek(0)
  elif format == 'mp3':
    mp3_stream = yt.streams.get_audio_only()
    file_stream = io.BytesIO()
    mp3_stream.stream_to_buffer(file_stream)
    file_stream.seek(0)

  # Send the file to the browser
  return send_file(file_stream, as_attachment=True, download_name=f'{yt.title}.{format}')


@app.route('/error')
def error():
    return render_template('error.html', message='Please fill in all fields!')

if __name__ == '__main__':
    app.run()
