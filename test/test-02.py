with open("data.txt", "r") as file:
    lines = file.readlines()

# Filter lines that contain the word "error" (case-insensitive)
error_lines = [line for line in lines if "error" in line.lower()]

# Print the matching lines
for line in error_lines:
    print(line.strip())

# Display the count of such lines
print(f"\nTotal lines containing 'error': {len(error_lines)}")

# Write the lines to a new file
with open("errors.log", "w") as log_file:
    log_file.writelines(error_lines)