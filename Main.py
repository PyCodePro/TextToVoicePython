# Import the gTTS library
from gtts import gTTS

# Open the text file and read the contents
with open('example.txt', 'r') as f:
    text = f.read()

# Create a gTTS object and specify the language
tts = gTTS(text=text, lang='en')

# Save the speech as an mp3 file
tts.save("example.mp3")
