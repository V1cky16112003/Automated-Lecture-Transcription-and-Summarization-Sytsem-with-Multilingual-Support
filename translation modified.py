from deep_translator import GoogleTranslator

with open("/Users/vigneshram/Documents/code/summary.txt", "r") as f:
    text = f.read()


languages = ["hi", "te", "ta", "ml"]


for lang in languages:
    try:
        
        translator = GoogleTranslator(source="auto", target=lang)
        translated_text = translator.translate(text)

        
        print(f"\nTranslated text in {lang}:")
        print(translated_text)

       
        with open(f"output_{lang}.txt", "w") as f:
            f.write(translated_text)

    except Exception as e:
        print(f"An error occurred while processing {lang}: {e}")