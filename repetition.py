def roll_again():
    print('Roll, roll, roll your boat')

    x = input('Do you want to roll your boat again?')

    if x.lower() == 'y':
        roll_again()              <------ This is what makes the repetition
    else:
        print('Done rolling.')

roll_again()

