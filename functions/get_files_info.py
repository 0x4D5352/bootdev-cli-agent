import os


def get_files_info(working_directory: str, directory: str=".") -> str:
    path: str = os.path.join(working_directory, directory)
    abspath = os.path.abspath(path)
    if not abspath.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    try:
        dir_contents = os.listdir(path)
        contents: list[str] = []
        for item in dir_contents:
            size = os.path.getsize(abspath + "/" + item)
            is_file = os.path.isfile(abspath + "/" + item)
            contents.append(f"- {item}: file_size={size} bytes, is_dir={is_file}")
        return "\n".join(contents)
    except Exception as e:
        return f"Error listing files: {e}"
