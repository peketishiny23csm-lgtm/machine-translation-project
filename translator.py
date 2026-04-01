from googletrans import Translator

translator = Translator()

text = input("Enter English sentence: ")

translated = translator.translate(text, src='en', dest='fr')

print("French:", translated.text)