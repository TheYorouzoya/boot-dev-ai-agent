import os

def get_file_content(working_directory, file_path):
    if file_path is None:
        return f"Error: File Path not provided"

    working_absolute_path = os.path.abspath("./" + working_directory)

    if not os.path.isdir(working_absolute_path):
        return f'Error: Working directory "{working_directory}" is not a directory'
    
    file_absolute_path = "/".join([working_absolute_path, file_path])

    if not file_absolute_path.startswith(working_absolute_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
    truncated = True

    try:
        with open(file_absolute_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            truncated = len(file_content_string) >= MAX_CHARS
            if truncated:
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string
    except FileNotFoundError:
        return f'Error: File "{file_path}" does not exist'
    except OSError as e:
        return f'Error: An error occured while reading file "{file_path}": {e}'