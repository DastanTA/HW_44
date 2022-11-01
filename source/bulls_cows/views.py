from django.shortcuts import render
from urllib.parse import parse_qs
from random import randint, sample


main_n = 4   # count of numbers that will be accepted

def guess_number(secret, actual):
    bulls = 0
    cows = 0
    to_response = {}

    if len(actual) != main_n:
        to_response['warning'] = f'Please enter exactly {main_n} digits! Separate them with spaces'

    for i in actual:
        counter = 1

        if 0 < i < 10:
            for j in actual:
                if i == j:
                    counter += 1
            if counter > 2:
                to_response['warning'] = 'There should not be similar digits. Only unique numbers!'
        else:
            to_response['warning'] = 'You can enter only digits between 1 and 9'

    for i in range(main_n):
        if secret[i] == actual[i]:
            bulls += 1

    for a in actual:
        if a in secret:
            cows += 1

    if bulls == main_n:
        secret_nums[:] = generate_numbers(main_n)
        print(f'Secret numbers: {secret_nums}')
        to_response['win_text'] = f'You got it right! You guessed all {main_n} numbers! \nGame over!'
    else:
        to_response['bulls'] = bulls
        to_response['cows'] = cows - bulls

    return to_response

def generate_numbers(n):
    return sample(range(1, 10), n)

secret_nums = generate_numbers(main_n)
print(f'Secret numbers: {secret_nums}')

def main_page(request):
    actual_nums = []
    to_response = {}

    if request.GET:
        numbers_lst_of_str = request.GET.get("guessing").split()
        try:
            for i in range(len(numbers_lst_of_str)):
                actual_nums.append(int(numbers_lst_of_str[i]))
        except ValueError:
            to_response["warning"] = "Please enter integers only"
        else:
            to_response = guess_number(secret_nums, actual_nums)
            print(to_response)
    else:
        to_response["warning"] = "Please, enter digits. Don't send empty form!"

    return render(request, 'index.html', to_response)
