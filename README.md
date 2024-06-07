Audio Transcription Project
---------------------------

This project transcribes audio files to text using OpenAI's Whisper model. The project is designed to be easy to use and set up, making it accessible for anyone who needs to convert audio files into readable text format.

### Project Structure

```
audio-transcript/
├── .gitignore
├── README.md
├── requirements.txt
├── transcribe.py
└── data/
    ├── input/
    ├── output/
    └── example_audio/

```

### Setup

**Prerequisites**

-   Python 3.6 or higher
-   pip (Python package installer)

**Installation**

1.  Clone the repository:

    Bash

    ```
    git clone https://github.com/lucianoaf8/audio-transcript.git
    ```

2.  Navigate to the project directory:

    Bash

    ```
    cd audio-transcript
    ```

3.  Install the required dependencies:

    Bash

    ```
    pip install -r requirements.txt
    ```

4.  Ensure ffmpeg is installed and added to your system path:

    -   Download and install ffmpeg from FFmpeg.org.
    -   Add ffmpeg to your system path.

**Usage**

1.  Place the audio files you want to transcribe in the `data/input` directory.

2.  Run the transcription script:

    Bash

    ```
    python transcribe.py
    ```

The transcriptions will be saved in the `data/output` directory with the same filename as the input audio file but with a `.txt` extension.

### Example

You can find example audio files in the `example_audio` directory to test the script.

### Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create a pull request or open an issue.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements

-   OpenAI Whisper - The transcription model used in this project.
-   FFmpeg - For handling audio file processing.

### Contact

If you have any questions or need further assistance, feel free to contact lucianoaf8@gmail.com.
