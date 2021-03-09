text = input("Text: ")

letters = sum(map(str.isalpha, text))
words = len(text.split())
sent = text.count('.') + text.count('!') + text.count('?')

index = round((5.88 * letters / words) - (29.6 * sent / words) - 15.8)

if index < 1:
    print("Before Grade 1")
elif index > 15:
    print("Grade 16+")
else:
    print(f"Grade {index}")