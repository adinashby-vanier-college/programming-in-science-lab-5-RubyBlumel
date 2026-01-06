def hollow_square(n):
    if n == 1:
        square = "*"
         return square
    elif n == 2: 
        square = ("**", "**")
        for square in square:
            return square
        
    elif n == 3:
        square = ("***", "* *", "***")
        for square in square:
            return square
    
    elif n == 5 
    square = ("*****", "*   *", "*   *", "*   *", "*****")
    for square in square
        return square
    
    else:    
        x = "*"
        y = " "

        print(x * n)
            
        count = 2
        while count <= n - 1:
            print(x, ((n - 4) * y), x)
            count += 1

        print(x * n)


        

# # 1
# # 12
# # 123
# # 1234
# def number_pattern(n):
#     return ""

# # Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
# def sum_of_natural_numbers(n):
#     return ""

# # Example for n = 4:
# #    *
# #   ***
# #  *****
# # *******
# def centered_star_pyramid(n):
#     return ""

hollow_square(3)
