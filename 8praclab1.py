# Program: Convert file content to uppercase

# Input file name
input_file = input("Enter source file name: ")

# Output file name
output_file = input("Enter destination file name: ")

try:
    with open(input_file, 'r') as f:
        content = f.read()

    # Convert to uppercase
    upper_content = content.upper()

    with open(output_file, 'w') as f:
        f.write(upper_content)

    print("\nContent written in uppercase successfully!")

    # Display output file content
    print("\n--- Output File Content ---")
    print(upper_content)

except FileNotFoundError:
    print("File not found. Please check the file name.")
