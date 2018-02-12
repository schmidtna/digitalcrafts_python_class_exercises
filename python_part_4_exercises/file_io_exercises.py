# I/O ex 1

# def opener():
file_name = input("Type your file name here:")
file_handle = open(file_name, "r")
file_handle.read()
file_handle.close()

    # if __name__ == "__main__":
    #     opener()