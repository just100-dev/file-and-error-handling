try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

# Index Error    
# my_list = [3, 5, 6]

# try:
#     print(my_list[7])
# except IndexError:
#     print("Error! Index out of range.")
    
# Key Error
# person = {"name": "Mark", "age": 30, "city": "New York"}

# try:
#     print(person["location"])
# except KeyError:
#     print("Error! Key not found.")
  
# Type Errors
# try:
#     print("name" + 25)  
# except TypeError:
#     print("Error! Cannot concatenate str and int.")

# File not found Error
# try:
#     with open("new_file.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Oooops! The file does not exist.")

try:
    with open("ddd.txt", "r") as file:
        print(file.read())
except Exception as e:
    print("Oooops! An error occured:", str(e))

