import traceback

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}") 
        traceback.print_exc()

def main():
    # Writing to a file
    write_to_file('sample.txt', 'Hello, World!\n')
    
    # Getting user input and writing to the file
    filename = input("Enter the filename to write to: ")
    data = input("Enter the data to write: ")
    write_to_file(filename, data)

if __name__ == "__main__":
    main()
