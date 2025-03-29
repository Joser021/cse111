import random
def main():
    numbers = [16.2, 75.1, 52.3]

    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    words = []

    append_random_words(words, 1)
    print(words)

    append_random_words(words, 5)

    print(words)
def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        decimal_numbers = random.uniform(10, 50)
        rounded = round(decimal_numbers, 1)
        numbers_list.append(rounded)
    
"""
stretch challenges
"""

def append_random_words(words_list, quantity=1):
    words = [
        "arm", "car", "cloud",
        "head", "heal", "hydrogen",
        "jog", "join", "laugh",
        "love", "sleep", "smile",
        "speak", "sunshine", "toothbrush",
        "tree", "truth", "walk", "water"
    ]

    for i in range(quantity):
        word = random.choice(words)
        words_list.append(word)


if __name__ == "__main__":
    main()