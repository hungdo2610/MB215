import traceback
def append_from_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

def main():
    filename = input("Enter the filename to append from: ")
    read_from_file(filename)

write_to_file('sample.txt', 'Hello, World!\n')

if __name__ == "__main__": # Call main() function if script is run directly
    main()