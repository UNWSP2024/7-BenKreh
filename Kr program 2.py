def display_larger_than_n_list(n, num_list):
    return [i for i in num_list if i > n]


my_list = list(range(1, 100))  
user_num = float(input("Input your number: "))
result = display_larger_than_n_list(user_num, my_list)
print(result)
