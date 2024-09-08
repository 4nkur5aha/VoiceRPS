import sounddevice as sd
import numpy as np
import speech_recognition as sr
import io
import random
import pyttsx3

def audio_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Record audio using sounddevice
    duration = 5  # seconds
    samplerate = 16000  # Hertz
    
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording complete.")
    
    # Convert the recorded audio data to an AudioData object
    audio_data = np.squeeze(audio_data)
    audio_data_bytes = audio_data.tobytes()
    audio_data_io = io.BytesIO(audio_data_bytes)

    # Create an AudioData object
    audio = sr.AudioData(audio_data_bytes, samplerate, 2)

    # Recognize speech using Google Web Speech API
    try:
        
        text = recognizer.recognize_google(audio)
        print(f"Your input:- {text}")
        return text
    
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

computer_wins = 0
user_wins = 0

choices = ["rock","paper","scissors"]

while True:
  print("Say Rock, Paper, Scissors or 'done' to end the game.")
  engine.say("Say Rock, Paper, Scissors or 'done' to end the game. ")
  engine.runAndWait()
  user_input = audio_to_text()
  print("")
  if user_input == "done":
    break

  if user_input not in choices:
    print("Invalid input, please enter a valid response.")
    engine.say("Invalid input, please enter a valid response.")
    print("")
    continue
  random_number = random.randint(0,2)
  computer_pick = choices[random_number]
  print("Computer picked " + computer_pick)
  engine.say("Computer picked " + computer_pick)
  engine.runAndWait()

  if user_input == "rock" and computer_pick == "scissors":
    print("Congrats! You have won this time! ")
    engine.say("Congrats! You have won this time! ")
    engine.runAndWait()
    
    print("")
    user_wins+=1
  
  elif user_input == "paper" and computer_pick == "rock":
    print("Congrats! You have won this time! ")
    engine.say("Congrats! You have won this time! ")
    engine.runAndWait()
    print("")
    user_wins+=1

  elif user_input == "scissors" and computer_pick == "paper":
    print("Congrats! You have won this time! ")
    engine.say("Congrats! You have won this time! ")
    engine.runAndWait()
    print("")
    user_wins+=1

  elif user_input == computer_pick:
    print("Oops! That's a tie! Points for both!")
    engine.say("Oops! That's a tie! Points for both!")
    engine.runAndWait()
    print("")
    user_wins+=1
    computer_wins+=1

  else:
    print("Alas! You have lost this time!")
    engine.say("Alas! You have lost this time!")
    engine.runAndWait()
    print("")
    computer_wins+=1

print("Computer won " + str(computer_wins) + " times and you have won " + str(user_wins) + " times")
engine.say("Computer won " + str(computer_wins) + " times and you have won " + str(user_wins) + " times")
engine.runAndWait()
print("")

if computer_wins > user_wins:
  print("Oh no, the computer has won in total! Try again later! ")
  engine.say("Oh no, the computer has won in total! Try again later! ")
  engine.runAndWait()
  
 
elif user_wins > computer_wins:
  print("Congrats! You have succesfully won the game in total! ")
  engine.say("Congrats! You have succesfully won the game in total! ")
  engine.runAndWait()
  

elif user_wins == computer_wins:
  print("That ended off with a tie! Nice try!")
  engine.say("That ended off with a tie! Nice try!")
  engine.runAndWait()
  






