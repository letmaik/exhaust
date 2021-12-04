import exhaustive

def generate_text(space: exhaustive.Space):
    use_emojis = space.maybe()
    space.note(("emojis", use_emojis))
    text = ""
    if use_emojis:
        text += "🤖" * 10
        text += "\n"
    language = space.choice(["en", "de"])
    space.note(("language", language))
    if language == "en":
        text += "Hello, world!"
    elif language == "de":
        text += "Hallo, Welt!"
    return text


for text, notes in exhaustive.iterate(generate_text, return_notes=True):
    notes = dict(notes)
    print(notes)
    print(text)
    print()

# Output:
# {'emojis': True, 'language': 'en'}
# 🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
# Hello, world!
#
# {'emojis': True, 'language': 'de'} 
# 🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
# Hallo, Welt!
#
# {'emojis': False, 'language': 'en'}
# Hello, world!
#
# {'emojis': False, 'language': 'de'}
# Hallo, Welt!
