def espresso(choice,resources):

    espresso = {
        'water': 200,
        'milk': 100,
        'coffee': 50,
    }

    if choice == 'espresso':
        print('\nThe Espresso is $1.5!')
        print('Please insert the coins!')
        quartes = int(input('How many quartes ($0.25)?'))
        dimes = int(input('How many dimes ($0.10)?'))
        nikles = int(input('How many nikles ($0.05)?'))
        pennies = int(input('How many pennies ($0.01)?'))
        money = (quartes * 0.25) + (dimes * 0.10) + (nikles * 0.05) + (pennies * 0.01)
        if money == 1.5 and espresso['water'] <= resources['water'] and espresso['milk'] <= resources['milk'] and espresso[
            'coffee'] <= resources['coffee']:
            resources['water'] -= espresso['water']
            resources['milk'] -= espresso['milk']
            resources['coffee'] -= espresso['coffee']
            resources['money'] += money
            print("\nThank you, here's your Espresso!")
        elif money > 1.5 and espresso['water'] <= resources['water'] and espresso['milk'] <= resources['milk'] and espresso[
            'coffee'] <= resources['coffee']:
            resources['water'] -= espresso['water']
            resources['milk'] -= espresso['milk']
            resources['coffee'] -= espresso['coffee']
            resources['money'] += money
            change = money - 1.5
            print("\nThank you, here's your Espresso!")
            print(f"Here your change: ${change:.2f}")
            resources['money'] -= change
        elif money >= 1.5 and espresso['water'] > resources['water'] or espresso['milk'] > resources['milk'] or espresso[
            'coffee'] > resources['coffee']:
            print("\nSorry machine out of resources!!")
            print(f"Here your change: ${money:.2f}")
        else:
            print("\nSorry not enough money!")
            print(f"Here your change: ${money:.2f}")