def imp(n):
    if(n > 500):
        print('Terminou')
    else:
        if(n % 5 == 0):
            print(n)
        n = n + 1
        imp(n)
imp(1)