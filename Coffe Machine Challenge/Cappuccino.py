def cappuccino(choice, resources):

    cappuccino = {
        'water': 100,
        'milk': 200,
        'coffee': 200,
    }

    if choice == 'cappuccino':
        print('\nThe Cappuccino is $2.5!')
        print('Please insert the coins!')
        quartes = int(input('How many quartes ($0.25)?'))
        dimes = int(input('How many dimes ($0.10)?'))
        nikles = int(input('How many nikles ($0.05)?'))
        pennies = int(input('How many pennies ($0.01)?'))
        money = (quartes * 0.25) + (dimes * 0.10) + (nikles * 0.05) + (pennies * 0.01)
        if money == 2.5 and cappuccino['water'] <= resources['water'] and cappuccino['milk'] <= resources['milk'] and cappuccino[
            'coffee'] <= resources['coffee']:
            resources['water'] -= cappuccino['water']
            resources['milk'] -= cappuccino['milk']
            resources['coffee'] -= cappuccino['coffee']
            resources['money'] += money
            print("\nThank you, here's your Cappuccino!")
        elif money > 2.5 and cappuccino['water'] <= resources['water'] and cappuccino['milk'] <= resources['milk'] and cappuccino[
            'coffee'] <= resources['coffee']:
            resources['water'] -= cappuccino['water']
            resources['milk'] -= cappuccino['milk']
            resources['coffee'] -= cappuccino['coffee']
            resources['money'] += money
            change = money - 2.5
            print("\nThank you, here's your Cappuccino!")
            print(f"Here your change: ${change:.2f}")
            resources['money'] -= change
        elif money >= 2.5 and cappuccino['water'] > resources['water'] or cappuccino['milk'] > resources['milk'] or cappuccino[
            'coffee'] > resources['coffee']:
            print("\nSorry machine out of resources!!")
            print(f"Here your change: ${money:.2f}")
        else:
            print("\nSorry not enough money!")
            print(f"Here your change: ${money:.2f}")