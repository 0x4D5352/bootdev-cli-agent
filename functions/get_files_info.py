import os


def get_files_info(working_directory, directory=".") -> str:
    abspath = os.path.abspath(directory)
    if not abspath.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a diretory'
    path = os.path.join(working_directory, directory)
    return ""
