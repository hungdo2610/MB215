
import traceback

def append_from_file(filename, data):
    try:
        with open(filename, 'a') as file:  # 'a' mode appends instead of overwriting
            file.write(data)
    except Exception as e:
        print(f"An error occurred while appending to the file: {filename}")
        traceback.print_exc()

# Example usage:
append_from_file('sample.txt', 'appended text.\n')


def main():
    filename = input("Enter the filename to append from: ")
    append_from_file(filename)



if __name__ == "__main__": # Call main() function if script is run directly
    main()