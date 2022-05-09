import random

test_words = ["all", "and", "any", "are", "bad", "bet", "big", "box", "boy", "bye", "bye",
              "can", "car", "cat", "cup", "cut", "dad", "day", "did", "dog", "dry", "eat",
              "eve", "fly", "for", "fun", "get", "had", "has", "her", "him", "his", "hot",
              "how", "hum", "let", "lot", "man", "may", "mom", "new", "not", "off", "old",
              "one", "our", "out", "pet", "put", "red", "run", "saw", "say", "see", "she",
              "sit", "the", "too", "top", "try", "two", "use", "was", "way", "who", "why",
              "yes", "yet", "you"
              ]

score = 0
i = 0

while i < 5:
    test = random.choice(test_words)
    print("Can you spell: " + test)

    word = input("Your turn! ")[:3]

    if word == test:
        score += 1
    else:
        print("Try again!")

    print("Score: " + str(score) + "\n")
    i += 1

