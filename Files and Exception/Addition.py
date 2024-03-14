print('Enter any two digits to get their sum')
print('Enter `q` to quit')

while True:
    num1 = input('Enter first digit:')
    if num1 == 'q':
        break
    num2 = input('Enter second digit:')
    if num2 == 'q':
        break

    try:
        answer = (int(num1) + int(num2))
    except ValueError:
        print('Enter only numbers!')
    else:
        print(answer)
