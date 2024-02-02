while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print(reply)
    else:
        print(int(reply)**2)
print('Good bye!')

while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    try:
        num = int(reply)
    except Exception:
        print('Bad! '*3)
    else:
        num = int(reply)
        if num < 18:
            print('You are under 18, so you are not allowed to enter')
        else:
            print(f'You are {num-18} year(s) older than you must be to enter, so you have access to the page')