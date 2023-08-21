Script written for a class, to transcribe audio notes into visible text.

This python script uses SpeechRecognition and Pydub libraries to perform an mp3 to txt transcription. This is performed by converting the MP3 file into WAV format using the Pydub library (This is performed in the function convert_mp3_to_wav). Then it uses the SpeechRecognition python library to transcribe the speech from the WAV file using the Google Web Speech API. THe text is then printed into the console.

Incomplete project. Although the script is fully functional. The script serves as a foundation for a website, which will allow users with an interactive interface for audio-to-text transcription.
