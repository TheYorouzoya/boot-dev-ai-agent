import os
import subprocess

def run_python_file(working_directory, file_path):
    if file_path is None or "":
        return f'Error: File not provided'
    
    if working_directory is None:
        return f'Error: Working directory not provided'
    
    working_absolute_path = os.path.abspath("./" + working_directory)

    if not os.path.isdir(working_absolute_path):
        return f'Error: Working directory "{working_directory}" is not a directory'
    
    file_absolute_path = os.path.abspath("/".join([working_absolute_path, file_path]))

    if not file_absolute_path.startswith(working_absolute_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted directory'
    
    if not file_absolute_path.endswith(".py"):
        return f'Error: File "{file_path}" is not a Python file.'

    if not os.path.exists(file_absolute_path):
        return f'Error: File "{file_path}" not found.'
    
    try:
        completed = subprocess.run(
            ["python3", file_absolute_path], 
            timeout=30,
            text=True,
            capture_output=True,
            cwd=working_absolute_path,)
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

    result = ""

    if completed.stdout is not None:
        result += f'STDOUT: {completed.stdout}'

    if completed.stderr is not None:
        result += f'\nSTDERR: {completed.stderr}'

    if completed.stdout is None and completed.stderr is None:
        result += "No output produced."

    if completed.returncode != 0:
        result += f"Process exited with code {completed.returncode}"

    return result
        
    