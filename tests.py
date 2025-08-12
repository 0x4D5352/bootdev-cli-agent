# from functions.write_file import write_file
# from functions.get_file_content import get_file_content
# from functions.get_files_info import get_files_info

def tests() -> None:
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

# def tests() -> None:
#     result = get_file_content("calculator", "main.py")
#     print(result)
#     result = get_file_content("calculator", "pkg/calculator.py")
#     print(result)
#     result = get_file_content("calculator", "/bin/cat")
#     print(result)
#     result = get_file_content("calculator", "pkg/does_not_exist.py")
#     print(result)
#
# def tests() -> None:
#     print('Result for current directory')
#     result = get_files_info("calculator", ".")
#     print(result)
#     print("Result for 'pkg' directory")
#     result = get_files_info("calculator", "pkg")
#     print(result)
#     print("Result for '/bin' directory")
#     result = get_files_info("calculator", "/bin")
#     print(result)
#     print("Result for '../' directory")
#     result = get_files_info("calculator", "../")
#     print(result)

if __name__ == "__main__":
    tests()
