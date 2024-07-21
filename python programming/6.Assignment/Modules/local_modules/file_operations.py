# file_operations.py

def read_file(file_path):
    
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def write_file(file_path, data):
    
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return "Write operation successful."
    except Exception as e:
        return f"An error occurred: {e}"

def append_to_file(file_path, data):
    
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        return "Append operation successful."
    except Exception as e:
        return f"An error occurred: {e}"
