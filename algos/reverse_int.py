#reverse integer

def reverse(x):
    if x > 0 :
        x = int(str(abs(x))[::-1])
        print('this is x', x)
        if x in range(-2**31, 2**31 - 1):
            print(x)
        else:
            print(0)
    else:
        x = int(str(abs(x))[::-1]) * -1
        if x in range(-2**31, 2**31 - 1):
            print(x)
        else:
            print(0)

reverse(1230)
int('1230')

#abs is to remove negative sign, absalute value
# cannot have leading 0 ints, abs 



