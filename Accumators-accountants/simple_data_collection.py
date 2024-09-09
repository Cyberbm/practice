men = 0
women = 0
older = ''
older_age = 0
other_gender = 0
men_names = []
women_names = []
other_names = []
#===================================================================
while True:
    print('==*==' * 10)
    name = input('Please Register your name [ Or press Q to quit ]: ').strip()
    print('==*==' * 10)
    if name.upper() == 'Q' or name.upper() == 'QUIT':
        break
    name = name.title()
#===================================================================
    while True:
        try:
            age = int(input(f'Please register your age, {name}: '))
            break
        except ValueError:
            print('Invalid input. Please enter a valid age.')
#===================================================================
    while True:
        gender = input('Register your gender [ M / F / Other ]: ').upper().strip()
        if gender in ['M', 'F', 'O', 'MALE', 'FEMALE', 'OTHER']:
            break
        else:
            print('Please, enter one of the options between [ M / F / Other ]')
#===================================================================
    if age > older_age:
        older_age = age
        older = name

    if gender == 'M' or gender == 'MALE':
        men += 1
        men_names.append(name)

    elif gender == 'F' or gender == 'FEMALE':
        women += 1
        women_names.append(name)

    elif gender == 'O' or gender == 'OTHER':
        other_gender += 1
        other_names.append(name)

    else:
        print('Please, enter a valid option.')
#===================================================================
#keeping the code safer against bugs or intentional empty registry
if men or women or other_gender:
    print(f'''The older person registered is {older}, with the age of {older_age} years old.
There is a total of {men} men registered, and their names are: {', '.join(men_names)}.
There is a total of {women} women registered, and their names are {', '.join(women_names)}.
There is a total of {other_gender} people registered as "other gender" and their names are {', '.join(other_names)}''')
else:
    print('No users were registered.')

