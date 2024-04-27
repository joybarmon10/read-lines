def read_notes_file(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []


# Example usage:
notes = read_notes_file("notes.txt")
if notes:
    print("Lines read from 'notes.txt':")
    for line in notes:
        print(line.strip())
