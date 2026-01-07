# Example for n = 5:

# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    if n == 1:
        square = "*"
        return square
   
    elif n == 3:
        square = ("***", "* *", "***")
        for square in square:
            return square
    else:    
        x = "*"
        y = " " 
        mult = x * n 
        count = 1
        while count <= n:
             result1 = (f"{x}{y * (n - 2)}{x}")
             count += 1

        return f"{mult}\n{result1}\n{mult}"
    #     mult = ((n - 2) * y) 
        
    # for mult in mult:
    #     mult = [n * mult]

            
            
            
    # result1 = f"{x}{mult}{x}"
           
            
        
    # return f"{result2}\n{result1}\n{result2}"
            
            
           

       

a = hollow_square(5)
print(a)

        

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
# #     return ""

