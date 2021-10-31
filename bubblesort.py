my_list = [1, 5, 6, 7, 8, 2]

for y in range(len(my_list)-1):
    x= 0
    while x < len(my_list)-1-y:
        if my_list[x] > my_list[x+1]:
            my_list[x], my_list[x+1] = my_list[x+1], my_list[x]
        else:
            x+=1
print(my_list)