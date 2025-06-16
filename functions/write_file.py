import os

def write_file(working_directory, file_path, content):
    if file_path is None:
        return f"Error: File Path not provided"
    
    working_absolute_path = os.path.abspath("./" + working_directory)

    if not os.path.isdir(working_absolute_path):
        return f'Error: Working directory "{working_directory}" is not a directory'
    
    file_absolute_path = os.path.abspath("/".join([working_absolute_path, file_path]))

    if not file_absolute_path.startswith(working_absolute_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(file_absolute_path, "w") as f:
            f.write(content)
    except OSError as e:
        return f'Error: An error occurred while writing to file "{file_path}": {e.strerror}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'