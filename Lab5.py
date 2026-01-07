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
   
    
    else:    
        x = "*"
        y = " " 
        mult = x * n 

        def new():
            return f"{x}{y * (n - 2)}{x}\n"
        

    return f"{mult}\n{new() * (n - 2)}{mult}"
        

# # 1
# # 12
# # 123
# # 1234

def number_pattern(n):
   
   result = ""
   for i in (range(1, (n + 1))):
       for j in range(1, i + 1):
          result += str(j)

       result += "\n"

    


   return result

 

       
      


# # # Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
# def sum_of_natural_numbers(n):
#     return ""

# # # Example for n = 4:
# # #    *
# # #   ***
# # #  *****
# # # *******
# def centered_star_pyramid(n):
#     return ""



