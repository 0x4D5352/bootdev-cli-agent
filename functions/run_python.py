import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] = []) -> str:
    path: str = os.path.join(working_directory, file_path)
    abspath = os.path.abspath(path)
    if not abspath.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(abspath):
        return f'Error: Cannot execute "{file_path}" as it is a directory, not a file'
    if not os.path.exists(abspath):
        return f'Error: File "{file_path}" not found.'
    _, ext = os.path.splitext(abspath)
    if ext != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python3", abspath,] + args, capture_output=True, timeout=30, text=True)
        out = f'STDOUT: {result.stdout}'
        err = f'STDERR: {result.stderr}'
        exit_code = ''
        if result.returncode > 0:
            exit_code = f'Process exited with code {result.returncode} '
        if out == '' and err == '':
            return 'No putput produced.'
        return f'{exit_code}{out} {err}'
    except Exception as e:
        return f"Error writing to file: {e}"
