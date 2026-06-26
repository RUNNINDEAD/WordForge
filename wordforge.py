import itertools
import random

# User Input

user_words = input(
    "Enter keywords separated by commas: "
)

keywords = [word.strip() for word in user_words.split(",") if word.strip()]

# Numbers and Special Char

numbers = [
    "",
    "1",
    "12",
    "123",
    "007",
    "2024",
    "2025",
]

specials = [
    "",
    "!",
    "@",
    "#",
    "$",
    "%",
    "&",
    "*",
    "_",
    "-",
]

# Set Max Passwords Generated
MAX_PASSWORDS = 1000000

capitalize_styles = [
    lambda x: x,
    lambda x: x.lower(),
    lambda x: x.upper(),
    lambda x: x.capitalize(),
]

passwords = set()

for word in keywords:
    for style in capitalize_styles:
        w = style(word)

        for num in numbers:
            for sp1, sp2 in itertools.product(specials, repeat=2):

                passwords.update([
                    f"{w}{num}{sp1}",
                    f"{sp1}{w}{num}",
                    f"{w}{sp1}{num}",
                    f"{w}{num}{sp1}{sp2}",
                    f"{num}{w}{sp1}",
                    f"{sp1}{num}{w}",
                    f"{w[::-1]}{num}{sp1}",   # reversed
                ])

passwords = list(passwords)
random.shuffle(passwords)

if len(passwords) > MAX_PASSWORDS:
    passwords = passwords[:MAX_PASSWORDS]

with open("passwords.txt", "w", encoding="utf-8") as f:
    for password in passwords:
        f.write(password + "\n")

print(f"\nGenerated {len(passwords)} passwords.")
print("Saved to passwords.txt")
