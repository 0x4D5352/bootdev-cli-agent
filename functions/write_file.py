import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    path: str = os.path.join(working_directory, file_path)
    abspath = os.path.abspath(path)
    if not abspath.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abspath):
        return f'Error: Cannot write to "{file_path}" as it is a directory, not a file'
    try:
        if os.path.exists(abspath):
            mode = "w"
        else:
            mode = "x"
        with open(abspath, mode) as f:
            content_length = f.write(content)
        return f'Successfully wrote to "{file_path}" ({content_length} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
