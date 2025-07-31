#  Part 1: File Read & Write Challenge 
def modify_file_fixed():
    """
    Reads 'text.txt', uppercases all content, and modifies the file
    """
    input_filename = "text.txt"
    output_filename = "text_modified.txt"

    try:
        with open(input_filename, "r") as file:
            lines = file.readlines()

        # Modify the content 
        modified_lines = [line.upper() for line in lines]

        with open(output_filename, "w") as new_file:
            new_file.writelines(modified_lines)

        print(f"'{input_filename}' modified and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"File '{input_filename}' not found.")
    except PermissionError:
        print(f"Permission denied for '{input_filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


#  Part 2: Error Handling Lab
def handle_file_input():
    """
    Asks the user for a filename and handles errors if it doesn't exist or can't be read.
    """
    filename = input("Enter the filename to test error handling: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Entry Point
if __name__ == "__main__":
        modify_file_fixed()
        handle_file_input()
