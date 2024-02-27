import os

if __name__ == "__main__":
    print(f"Starting file-management...\n")

    my_path = '/Users/lukepaez/Downloads'

    if os.path.isdir(my_path):
        print(f"Directory exists!")
    else:
        print(f"Directory not found!")
    