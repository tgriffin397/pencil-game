import random

name1 = 'John'
name2 = 'Jack'
first_player = ''
second_player = ''
num_pencils = ""


def start():
    global num_pencils
    global first_player
    global second_player

    while True:
        print('How many pencils would you like to use:')
        num_pencils = input()
        if num_pencils == '0':
            print('The number of pencils should be positive')
            continue
        elif not num_pencils.isdigit():
            print("The number of pencils should be numeric")
            continue
        else:
            num_pencils = int(num_pencils)
            break

    while True:
        print(f'Who will be the first ({name1}, {name2}):')
        name_choice = input()
        if name_choice == name1:
            first_player = name1
            second_player = name2
            break
        elif name_choice == name2:
            first_player = name2
            second_player = name1
            break
        else:
            print(f'Choose between {name1} and {name2}')
            continue

    print('|' * num_pencils)


def jack_bot():
    section = int(num_pencils) / 4
    if int(num_pencils) == 1:
        print('1')
        return '1'
    elif int(num_pencils) % 4 == 0:
        print('3')
        return '3'
    elif '.75' in str(section):
        print('2')
        return '2'
    elif '.50' in str(section) or '.5' in str(section):
        print('1')
        return '1'
    else:
        result = str(random.randint(1, 3))
        print(result)
        return result


def gameplay():
    global num_pencils
    count = 0
    current_player = ""
    while num_pencils > 0:
        if count % 2 == 0:
            print(f"{first_player}'s turn:")
            current_player = first_player
        else:
            print(f"{second_player}'s turn:")
            current_player = second_player
        while True:
            accepted_values = ['1', '2', '3']

            if current_player == name1:
                user = input()
            else:
                user = jack_bot()

            if user not in accepted_values:
                print(f"Possible values: '{accepted_values[0]}', '{accepted_values[1]}' or '{accepted_values[2]}'")
                continue
            elif int(user) > int(num_pencils):
                print('Too many pencils were taken')
                continue
            elif int(user) == int(num_pencils):
                if count % 2 == 0:
                    print(f"{second_player} won!")
                    return
                else:
                    print(f"{first_player} won!")
                    return
            else:
                count += 1
                num_pencils -= int(user)
                print('|' * num_pencils)
                break


def motor():
    start()
    gameplay()


motor()
