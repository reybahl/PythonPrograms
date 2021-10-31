def is_power(num1, num2):
    """ num1 is  the big number, 
    and num2 is  the small number. 
    This functions finds if num1 is 
    a power of num2"""
    
    div = num1 / num2

    while True:
        div = div / num2

        if div == 1:
            return True
        elif div < 1:
            return False

print(is_power(int(input()), int(input())))