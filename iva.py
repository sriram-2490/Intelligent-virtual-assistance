import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import openai
import tkinter as tk

# Initialize speech recognition and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# OpenAI API key (replace with your own API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to log and talk
def talk(text):
    print(text)  # Print what is being spoken
    engine.say(text)
    engine.runAndWait()
    log_conversation(text)  # Log the conversation

# Function to log conversations to a text file
def log_conversation(text):
    with open("conversation_log.txt", "a") as log_file:
        log_file.write(text + "\n")

# Function to take user command through speech
def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'iva' in command:
                command = command.replace('iva', '')  # Removing 'iva' from the command
                print("User said:", command)
    except Exception as e:
        print("Sorry, I didn't hear that. Can you please repeat?")
        pass
    return command

# Function to get a response from OpenAI's GPT-3 model
def chat_with_gpt(user_message, conversation_history):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
            messages=conversation_history + [{"role": "user", "content": user_message}],
            max_tokens=150,
            temperature=0.7
        )
        gpt_response = response['choices'][0]['message']['content']
        return gpt_response
    except Exception as e:
        print(f"Error with GPT API: {e}")
        return "Sorry, I couldn't process that. Please try again."

# Function to handle "How about you?" and similar queries
def handle_friendly_responses(command):
    # Responses for friendly greetings and common questions
    if 'how about you' in command:
        talk("I'm fine, thank you for asking! How about you?")
    elif 'how are you' in command:
        talk("I'm doing great, thanks for asking! How are you?")
    elif 'i am fine' in command or 'i am doing great' in command:
        talk("Thanks for letting me know! I'm glad to hear you're doing well.")
    elif 'hello' in command:
        talk("Hello! How can I help you today? I'm Iva, your friendly assistant.")
    else:
        return False  # Not a friendly response, so continue to chat with GPT
    return True

# Function to open websites based on command
def open_website(command):
    if 'youtube' in command:
        webbrowser.open('https://www.youtube.com')
        talk("Opening YouTube.")
    elif 'google' in command:
        webbrowser.open('https://www.google.com')
        talk("Opening Google.")
    elif 'wikipedia' in command:
        webbrowser.open('https://www.wikipedia.org')
        talk("Opening Wikipedia.")
    else:
        return False  # No website match found
    return True

# Function to handle music, time, jokes, etc.
def handle_miscellaneous_commands(command):
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}.")
    elif 'who the heck is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    elif 'date' in command:
        talk('Sorry, I have a headache today.')
    elif 'quit' in command or 'exit' in command:
        talk("Goodbye! See you next time.")
        root.quit()  # Exit the program
    else:
        return False
    return True

# Main function to run assistant
def run_assistant():
    conversation_history = [{"role": "system", "content": "You are a friendly and helpful assistant named Iva."}]
    
    # Start listening
    command = take_command()
    print("Command received:", command)

    # Handle friendly responses like "How are you?"
    if handle_friendly_responses(command):
        pass  # We already handled this response

    # Handle website opening commands like "Open YouTube"
    elif open_website(command):
        pass  # Website has been opened

    # Handle music, time, jokes, etc.
    elif handle_miscellaneous_commands(command):
        pass  # Miscellaneous command has been processed

    else:
        # ChatGPT-based response for general queries
        gpt_response = chat_with_gpt(command, conversation_history)
        talk(gpt_response)
        conversation_history.append({"role": "user", "content": command})
        conversation_history.append({"role": "assistant", "content": gpt_response})

# Setting up the Tkinter window for the button
root = tk.Tk()
root.title("Iva Assistant")

# Button to activate Iva's listening
def on_button_click():
    run_assistant()

button = tk.Button(root, text="Talk to Iva", command=on_button_click, height=2, width=20)
button.pack(pady=20)

# Greet the user at the start
talk("Hello, I'm Iva, your assistant. How can I help you today?")

# Run the Tkinter event loop
root.mainloop()
