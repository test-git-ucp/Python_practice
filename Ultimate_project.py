# import pygame
# #print("Pygame version:",pygame.__version__)
# import os
# import time
# from gtts import gTTS
# from langdetect import detect
# from googletrans import Translator
# pygame.mixer.init()
# def main():
#     print("Welcome to Music Player with Translation!")
    
#     while True:
#         print("\nOptions:")
#         print("1. Play a song")
#         print("2. Speak text")
#         print("3. Translate text")
#         print("4. Exit")
        
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == "1":
#             # Music play logic
#             song_path = input("Enter song file path: ")
#             if os.path.exists(song_path):
#                 play_music(song_path)
#             else:
#                 print("File not found!")
                
#         elif choice == "2":
#             # Text to speech logic
#             text = input("Enter text to speak: ")
#             lang = input("Enter language code (en, hi, es, etc.) or press enter for auto-detection: ")
            
#             if lang:
#                 text_to_speech(text, lang)
#             else:
#                 detected_lang = detect_language(text)
#                 print(f"Detected language: {detected_lang}")
#                 # You'll need to map language name to code here
#                 text_to_speech(text, 'en')  # Default to English for now
                
#         elif choice == "3":
#             # Translation logic
#             text = input("Enter text to translate: ")
#             dest_lang = input("Enter target language code (en, hi, es, etc.): ")
            
#             translated_text = translate_text(text, dest_lang)
#             print(f"Translated text: {translated_text}")
            
#             speak = input("Do you want to hear the translation? (y/n): ")
#             if speak.lower() == 'y':
#                 text_to_speech(translated_text, dest_lang)
                
#         elif choice == "4":
#             print("Goodbye!")
#             break
            
#         else:
#             print("Invalid choice. Please try again.")
# if __name__=="__main__":
#     main()
# def play_music(file_path):
    
#     """
#     this funstion play music rom the given path
#     """
#     try:
#         pygame.mixer.music.load(file_path)
#         pygame.mixer.music.play()
#         print(f"playing:{os.path.basename(file_path)}")
#     except Exception as e:
#         print("error playing music:")
    
# def text_to_speech(text,language='en'):
#     try:
#         tts=gTTS(text=text,lang=language)
#         tts.save("temp_speech.mp3")
#         play_music("temp_speech.mp3")
#     except Exception as e:
#         print(f"Text_to_speech error:{e}")
# def detect_language(text):
#     """
#     Detect the language of the given text
#     """
#     try:
#         lang_code = detect(text)
#         # Convert language code to full name
#         lang_map = {'en': 'English', 'hi': 'Hindi', 'es': 'Spanish', 
#                    'fr': 'French', 'de': 'German', 'ja': 'Japanese'}
#         return lang_map.get(lang_code, 'Unknown')
#     except:
#         return "Unknown"
# def translate_text(text, dest_language='en'):
#     """
#     Translate text to the destination language
#     """
#     try:
#         translator = Translator()
#         translation = translator.translate(text, dest=dest_language)
#         return translation.text
#     except Exception as e:
#         print(f"Error in translation: {e}")
#         return text

    







