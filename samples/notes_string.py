import exhaustive

def generate_text(space: exhaustive.Space):
    use_emojis = space.maybe()
    space.note(f"emojis={'yes' if use_emojis else 'no'}")
    text = ""
    if use_emojis:
        text += "🤖" * 10
        text += "\n"
    language = space.choice(["en", "de"])
    space.note(f"language={language}")
    if language == "en":
        text += "Hello, world!"
    elif language == "de":
        text += "Hallo, Welt!"
    return text


for text, notes in exhaustive.iterate(generate_text, return_notes=True):
    print(", ".join(notes))
    print(text)
    print()

# Output:
# emojis=yes, language=en
# 🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
# Hello, world!
#
# emojis=yes, language=de
# 🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
# Hallo, Welt!
#
# emojis=no, language=en
# Hello, world!
#
# emojis=no, language=de
# Hallo, Welt!
