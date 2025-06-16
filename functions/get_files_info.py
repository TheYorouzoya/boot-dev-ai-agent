import os

def get_files_info(working_directory, directory=None):
    working_absolute_path = os.path.abspath("./" + working_directory)

    if not os.path.isdir(working_absolute_path):
        return f'Error: Working directory "{working_directory}" is not a directory'

    if directory is None:
        directory = ""

    directory_path = "/".join([working_absolute_path, directory])

    directory_absolute_path = os.path.abspath(directory_path)

    if not directory_absolute_path.startswith(working_absolute_path):
        return f'Error: Canot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory_absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    contents = os.listdir(directory_absolute_path)

    result = ""

    for content in contents:
        content_path = os.path.join(directory_absolute_path, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        result += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"

    return result