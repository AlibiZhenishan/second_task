def name ():
    supname = 0
    while supname == 0:
        name = input('What is your name? ')
        print('Is your name ', name, 'yes/no')
        a = input()
        if a =='yes':
            supname = 1
    print('Hello', name)
name()
