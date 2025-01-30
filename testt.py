words = [
    "luxuriant", "silly", "dizzy", "frightening", "blink", "silly",
    "enjoy", "suspend", "blink", "reward", "blink", "fact", "debt",
    "marble", "blink", "yak", "frightening", "suspend", "debt"
]

# Създаване на речник за преброяване на думите
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Извеждаме хистограмата
for word, count in word_count.items():
    print(f"{word}|{'*' * count}")
