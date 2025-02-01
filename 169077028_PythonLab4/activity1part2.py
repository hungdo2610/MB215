import traceback
def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

def main():
    filename = input("Enter the filename to read from: ")
    read_from_file(filename)

if __name__ == "__main__": # Call main() function if script is run directly
    main()