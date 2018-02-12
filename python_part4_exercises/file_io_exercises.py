# I/O ex 1



# file_input = input("Type file name:")

# file_handle = open(file_input, "r")
# contents = file_handle.read()
# print(contents)
# file_handle.close()

    
# def file_opener():

#     file_search = input("Type file name:")

#     with open(file_search, "r") as file_handle:
#         contents = file_handle.read()

#     print(contents)

# if __name__ == "__main__":
#     file_opener()

# I/O ex 2
        
def file_writer():

    file_search = input("Type file name:")

    with open(file_search, "w") as file_handle:
        contents = input("Type some info into this file:")
        file_handle.write(contents)

    

if __name__ == "__main__":
    file_writer()