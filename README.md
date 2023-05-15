# Jarvis - Voice Assistant

Jarvis is a simple voice assistant program written in Python. It uses speech recognition and text-to-speech conversion to interact with the user and perform various tasks.

## Requirements

To run this program, you need to have the following dependencies installed:

- pyttsx3
- SpeechRecognition
- wikipedia
- webbrowser

You can install these dependencies using pip: pip install pyttsx3 SpeechRecognition wikipedia webbrowser


## Usage

1. Clone the repository or download the source code.

2. Install the required dependencies as mentioned in the Requirements section.

3. Run the `voice_assistant.py` file

4. Jarvis will greet you and wait for your command.

5. Speak your command to perform various tasks such as searching on Wikipedia, opening websites, getting the current time, and more.

6. To stop Jarvis, say "stop" or press Ctrl+C.

## Supported Commands

Jarvis supports the following commands:

- **Wikipedia**: You can ask Jarvis to search for a topic on Wikipedia, and it will provide a summary of the results.

- **Open YouTube**: Jarvis opens the YouTube website in your default web browser.

- **Open Google**: Jarvis opens the Google website in your default web browser.

- **Open Notepad**: Jarvis opens the Notepad application.

- **Open Command Prompt**: Jarvis opens the Command Prompt.

- **Open Stack Overflow**: Jarvis opens the Stack Overflow website in your default web browser.

- **Open Calendar**: Jarvis opens a website related to calendars in your default web browser.

- **Open Code**: Jarvis opens the Visual Studio Code application.

- **Time**: Jarvis tells you the current time.

- **Stop**: Jarvis stops and exits the program.

If you give a command that is not recognized, Jarvis will inform you that the command is unregistered.

## Customize and Extend

You can customize and extend Jarvis according to your needs. The code provides a basic structure for handling voice commands and performing corresponding actions. You can add new commands, integrate additional APIs or services, or modify the existing functionality.

Feel free to explore the code and make changes as per your requirements.
