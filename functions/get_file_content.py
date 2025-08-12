from .config import MAX_CHARS
import os

def get_file_content(working_directory: str, file_path: str) -> str:
    path: str = os.path.join(working_directory, file_path)
    abspath = os.path.abspath(path)
    if not abspath.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abspath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abspath, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            total_file_length = len(f.read())
        result: str = file_content_string
        if total_file_length > MAX_CHARS:
            result += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return result
    except Exception as e:
        return f"Error reading file: {e}"
