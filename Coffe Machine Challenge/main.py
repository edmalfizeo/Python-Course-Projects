import Espresso, Latte, Cappuccino, Art

CoffeMachine = True

resources = {
    'water': 1000,
    'milk': 1000,
    'coffee': 1000,
    'money': 0,
}

while CoffeMachine:
    print('-' * 30)
    print('Welcome to Coffee Machine!')
    print(Art.logo)
    print('-' * 30)
    choice = input('\nWhat would you like to drink? (Espresso/Latte/Cappuccino)').lower()

    Espresso.espresso(choice, resources)
    Latte.latte(choice, resources)
    Cappuccino.cappuccino(choice, resources)

    if choice == 'report':
        print('-' * 30)
        for key, value in resources.items():
            if key not in ['coffee', 'money']:
                print(f'{key}: {value}ml')
            elif key == 'coffee':
                print(f'{key}: {value}g')
            else:
                print(f'{key}: ${value}')

    if choice == 'off':
        CoffeMachine = False
