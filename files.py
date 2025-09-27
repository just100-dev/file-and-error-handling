# 1. Read Mode
# file = open("test.txt", "r")
# read_file = file.read()
# print(read_file)
# file.close()

# Write Mode
# file = open("test.txt", "w")
# file.write("This is the replaced line of words \nThis is a second Line \nThis is a third Line")
# file.close()

# 3. Append Mode
# file = open("test.txt", "a")
# file.write("\nThis is an appended Line")

# 4. Create Mode
# file = open("new_file.txt", "w")
# file.write("New file succesfully created")
# file.close()

with open("new_file.txt", "w") as f:
    f.write("New best practices succesfully created")
    
with open("new_file.txt", "a") as file:
    file.write("\nNew Line added")



