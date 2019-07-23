# Part 2 of the Python Review lab.

def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def encode(x, y):
    while 1 < y < 250 and 500 < x < 1000:
        while not is_prime(x):
            x+=1

        while not is_prime(y):
            y+=1

        product = x + y
        return product

    print("Ivalid input: Outside range.")
    return None

def decode(coded_message):
    num = coded_message
    for i in range(1, 250):
        for j in range(500, 1000):
            if is_prime(i) and is_prime(j) and i+j == num:
                print("x is %d ; y is %d" % (j , i))

x , y = 789 , 45
encode(x,y)
decode(encode(x, y))


        
