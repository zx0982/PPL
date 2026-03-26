# Program: Copy python file without comments

def remove_comments(line):
    # Remove inline comments
    if '#' in line:
        return line[:line.index('#')]
    return line


# Take file names from user
source = input("Enter source Python file: ")
destination = input("Enter destination file: ")

try:
    with open(source, 'r') as src, open(destination, 'w') as dest:

        print("\n--- Source File Content ---")

        for line in src:
            print(line, end="")  # Print original content

            clean_line = remove_comments(line).strip()

            if clean_line:  # Avoid empty lines
                dest.write(clean_line + '\n')

    # Display destination content
    print("\n\n--- Destination File Content (Without Comments) ---")

    with open(destination, 'r') as dest:
        print(dest.read())

    print("\nFile copied successfully without comments!")

except FileNotFoundError:
    print("File not found. Please check the file name.")
