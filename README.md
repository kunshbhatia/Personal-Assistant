# David - Your Voice-Activated Python Assistant

David is a voice-controlled desktop assistant built in Python. It uses speech recognition and text-to-speech to interact with the user and perform a range of helpful tasks including opening applications, browsing the web, searching Wikipedia, providing time-based reminders, and more. The assistant greets you based on the current time and listens continuously for your commands until instructed to stop.

---

## Features

* **Voice Interaction**: Accepts spoken commands and responds using text-to-speech.
* **Wikipedia Search**: Fetches and reads summaries from Wikipedia.
* **Web Automation**: Opens commonly used websites like YouTube and Spotify in the default browser.
* **Time Reporting**: Tells the current system time on request.
* **Reminders**: Can set short-term reminders for 1, 5, or 10 minutes.
* **App Launching**: Opens installed applications by voice using the `AppOpener` library.
* **Contextual Responses**: Responds to compliments or negative feedback.

---

## Technologies Used

* `speech_recognition`: Converts spoken commands to text.
* `pyttsx3`: Converts text to speech (offline).
* `wikipedia`: Fetches summary data from Wikipedia.
* `webbrowser`: Launches websites.
* `datetime` and `time`: For time-based features.
* `AppOpener`: Opens installed desktop applications.
* Python's built-in control flow and error handling.

---

## Getting Started

###  Prerequisites

Install the required packages using pip:

```bash
pip install pyttsx3 SpeechRecognition wikipedia AppOpener
```

> You may also need to install `pyaudio` (used by `speech_recognition`):

```bash
pip install pyaudio
```

If `pyaudio` fails on Windows, install via `.whl` from [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

## How to Run

1. Make sure your microphone is working.
2. Open a terminal or run from your IDE.
3. Run the Python script:

```bash
python mycode.py
```

4. Start giving commands like:

   * "Open YouTube"
   * "Search machine learning on Wikipedia"
   * "What is the current time?"
   * "Reminder for 1"
   * "Stop"

---

## Example Commands

| Command                     | Action                          |
| --------------------------- | ------------------------------- |
| `open youtube`              | Opens YouTube in browser        |
| `wikipedia Albert Einstein` | Speaks a summary from Wikipedia |
| `current time`              | Tells the current time          |
| `reminder for 1`            | Reminds after 1 minute          |
| `open chrome`               | Opens Google Chrome             |
| `stop` or `quit`            | Exits the assistant             |

---

## Notes

* Only works in English (`en-in` language set for Google recognizer).
* The assistant runs in an infinite loop until stopped by voice.
* Make sure you're connected to the internet for voice recognition and Wikipedia search.
* Works best on **Windows** (due to SAPI5 voice engine used by `pyttsx3`).


