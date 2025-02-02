import traceback
def read_from_file(filename, data):
    try:
        with open(filename, 'r') as file:
            file.read(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

def main():
    filename = input("Enter the filename to read from: ")
    read_from_file(filename)
    non_existent_content = read_from_file('non_existent_file.txt')
    if non_existent_content is None:
        print("Could not read the non-existent file.")



if __name__ == "__main__": # Call main() function if script is run directly
    main()
    

