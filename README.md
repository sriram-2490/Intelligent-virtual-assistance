# Iva - Your Friendly AI Assistant

**Iva** is a voice-activated personal assistant built using Python, OpenAI GPT-3, and several other Python libraries. Iva can chat with you, open websites, tell jokes, play music, and respond to various commands in a friendly way.

## Features

- **Voice Recognition**: Iva listens to your commands through speech input.
- **Friendly Conversations**: Iva can respond to "How are you?", "What's up?", and other casual greetings.
- **Open Websites**: Iva can open websites like YouTube, Google, Wikipedia, etc.
- **Play Music**: Iva can play songs using YouTube.
- **Tell Jokes**: Iva can tell jokes to keep you entertained.
- **Real-Time Information**: Iva can tell the time and date, as well as provide information from Wikipedia.
- **GPT-3 Integration**: For more complex queries, Iva uses OpenAI's GPT-3 to provide intelligent responses.
- **GUI Integration**: You can interact with Iva using a button in a graphical user interface (GUI).

## Requirements

Before running Iva, you need to install the following Python libraries:

- `speech_recognition`: For recognizing speech input.
- `pyttsx3`: For text-to-speech functionality.
- `pywhatkit`: For playing music and opening websites.
- `wikipedia`: To fetch information from Wikipedia.
- `pyjokes`: For telling jokes.
- `openai`: For integrating OpenAI GPT-3.
- `tkinter`: For creating the GUI (comes pre-installed with Python).
- `pyaudio`: This is required for microphone support in `speech_recognition`.

You can install the required dependencies using `pip`:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes openai pyaudio
