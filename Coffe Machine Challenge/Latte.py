def latte(choice, resources):

    latte = {
        'water': 200,
        'milk': 200,
        'coffee': 100,
    }

    if choice == 'latte':
        print('\nThe Latte is $2.0!')
        print('Please insert the coins!')
        quartes = int(input('How many quartes ($0.25)?'))
        dimes = int(input('How many dimes ($0.10)?'))
        nikles = int(input('How many nikles ($0.05)?'))
        pennies = int(input('How many pennies ($0.01)?'))
        money = (quartes * 0.25) + (dimes * 0.10) + (nikles * 0.05) + (pennies * 0.01)
        if money == 2.0 and latte['water'] <= resources['water'] and latte['milk'] <= resources['milk'] and latte[
            'coffee'] <= resources['coffee']:
            resources['water'] -= latte['water']
            resources['milk'] -= latte['milk']
            resources['coffee'] -= latte['coffee']
            resources['money'] += money
            print("\nThank you, here's your Latte!")
        elif money > 2.0 and latte['water'] <= resources['water'] and latte['milk'] <= resources['milk'] and latte[
            'coffee'] <= resources['coffee']:
            resources['water'] -= latte['water']
            resources['milk'] -= latte['milk']
            resources['coffee'] -= latte['coffee']
            resources['money'] += money
            change = money - 2.0
            print("\nThank you, here's your Latte!")
            print(f"Here your change: ${change:.2f}")
            resources['money'] -= change
        elif money >= 2.0 and latte['water'] > resources['water'] or latte['milk'] > resources['milk'] or latte[
            'coffee'] > resources['coffee']:
            print("\nSorry machine out of resources!!")
            print(f"Here your change: ${money:.2f}")
        else:
            print("\nSorry not enough money!")
            print(f"Here your change: ${money:.2f}")