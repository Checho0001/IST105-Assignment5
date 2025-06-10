from django.shortcuts import render
from .forms import PuzzleForm
import random

def calculate(request):
    result = {}
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            result['number'] = number
            text = form.cleaned_data['text']
            result['text'] = text


            # Number Puzzle
            if number % 2 == 0:
                result['parity'] = 'Even'
                result['number_result'] = number ** 0.5
                result['number_op'] = 'Square Root'
            else:
                result['parity'] = 'Odd'
                result['number_result'] = number ** 3
                result['number_op'] = 'Cube'

            # Text Puzzle
            binary = ' '.join(format(ord(char), '08b') for char in text)
            vowels = sum(char.lower() in 'aeiou' for char in text)
            result['binary'] = binary
            result['vowel_count'] = vowels

            # Treasure Hunt
            target = random.randint(1, 100)
            guesses = []
            won = False
            for i in range(1, 6):
                guess = random.randint(1, 100)
                guesses.append(guess)
                if guess == target:
                    won = True
                    break
            result['treasure_target'] = target
            result['guesses'] = guesses[:i]
            result['win'] = won

    else:
        form = PuzzleForm()

    return render(request, 'puzzle/results.html', {'form': form, 'result': result})
