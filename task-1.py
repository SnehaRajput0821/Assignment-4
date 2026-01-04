# Task 1: Read a File and Handle Errors

try:
    # Attempt to open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line one by one
        for line in file:
            print(line.strip())  # strip() removes extra newline characters
except FileNotFoundError:
    # Handle the case where the file does not exist
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
