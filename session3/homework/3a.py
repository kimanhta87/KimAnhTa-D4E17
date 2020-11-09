import random

WORDS = ('python', 'jumble', 'easy', 'difficult', 'answer', 'xylopphone')

word = random.choice(WORDS)

correct = word

jumble = ''

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position +1)]
    score = 0
    print \
    