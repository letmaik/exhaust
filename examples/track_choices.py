# This example shows how to track choices and return them
# together with the generated items.

import exhaust

def generate_text(state: exhaust.State):
    choices = {}
    choices['use_emojis'] = state.maybe()
    text = ""
    if choices['use_emojis']:
        text += "🤖" * 10
        text += "\n"
    choices['language'] = state.choice(["en", "de"])
    if choices['language'] == "en":
        text += "Hello, world!"
    elif choices['language'] == "de":
        text += "Hallo, Welt!"
    return text, choices


for text, choices in exhaust.space(generate_text):
    print(choices)
    print(text)
    print()

# Output:
# {'use_emojis': True, 'language': 'en'}
# 🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
# Hello, world!       
#
# {'use_emojis': True, 'language': 'de'}
# 🤖🤖🤖🤖🤖🤖🤖🤖🤖🤖
# Hallo, Welt!
#
# {'use_emojis': False, 'language': 'en'}
# Hello, world!
#
# {'use_emojis': False, 'language': 'de'}
# Hallo, Welt!
