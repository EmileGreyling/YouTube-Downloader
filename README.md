<p align="center">
  <img src="https://capsule-render.vercel.app/api?text=YouTube%20Downloader&animation=fadeIn&type=soft&color=gradient&height=150"/>
</p>


### This project is a YouTube video downloader web application built using the Flask framework. It allows users to input a YouTube video URL and download the video in the available formats. This README.md file provides an overview of the project, installation instructions, usage guide, and potential areas for improvement.

⚠️ **Note:** Downloading copyrighted content from YouTube without proper authorization may violate YouTube's terms of service and copyright laws. This project is meant for educational purposes and personal use only. Be sure to respect the rights of content creators and follow all applicable laws.

## 🚀 Features 

🎉 Input a valid YouTube video URL.

📺 Choose from a list of available formats.

⬇️ Download the selected video to your local machine.

## ⚙️ Installation 

Follow these steps to set up and run the YouTube Video Downloader:

1. Clone the repository:

   ```bash
   git clone https://github.com/EmileGreyling/YouTube-Downloader-In-Flask.git
2. Navigate to the project directory:

    ```bash
    cd YouTube-Downloader-In-Flask
3. Create a virtual environment
    ```bash
    python3 -m venv env
4. Activate the virtual environment:
    - On Windows:
      ```bash
      env\Scripts\activate
    - On macOS and Linux:
      ```bash
      source env/bin/activate
5. Install required dependencies:
    ```bash
    pip install -r requirements.txt
6. Run the Flask application:
    ``bash
    flask run
7. Open a web browser to `http:127.0.0.1:5000` to access the application.

## 📝 Usage 

1. Enter a valid YouTube video URL in the input field.
2. Select the desired format (mp4 or mp3)
3. Click the "Download" button and wait for the video to downlaod.
4. The file will be downloaded to your default download location.


## 🤝 Contributing 
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Submit a pull request explaining your changes.


## 🌟 Improvements 
Here are some potential areas for improvement in the project:

- [ ] User Interface: Enhance the user interface to make it more intuitive and visually appealing using HTML, CSS, and JavaScript.

- [ ] Error Handling: Implement better error handling for cases where the provided URL is invalid or the video format is not supported.

- [ ] Download Progress: Provide real-time download progress to the user.

- [ ] Support for Other Platforms: Extend the application's functionality to support video downloads from other platforms.
