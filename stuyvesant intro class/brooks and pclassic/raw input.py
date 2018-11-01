def get():
    while True:
        c = raw_input('input name? (Y/N)')
        if c == 'Y' or c == 'y':
            n = raw_input('name:')
        elif c == 'N' or c == 'n':
            break
        else:
            print('Error')
            break
