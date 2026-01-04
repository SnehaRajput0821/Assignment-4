# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to output.txt
user_input = input("Enter some text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")   # write user input with newline

print("Data written to output.txt successfully.")

# Step 2: Append additional data to the same file
append_data = input("Enter additional text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(append_data + "\n")  # append new data

print("Additional data appended to output.txt successfully.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())