def read_and_write_file():
    try:
        filename = input("Enter the filename to read: ")
        
        # Open the input file in read mode
        with open(filename, 'r') as infile:
            content = infile.read()
        
        # Modify content - example: convert it to uppercase
        modified_content = content.upper()
        
        # Write modified content to a new file
        with open('modified_' + filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to 'modified_{filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the file read/write function
read_and_write_file()

