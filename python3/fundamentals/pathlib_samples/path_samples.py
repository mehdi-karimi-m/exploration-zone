from pathlib import Path
from pprint import pprint

Path("C:\\Program Files\\Microsoft")
Path(r"C:\Program Files\Microsoft")
Path("/usr/local/bin")
Path()  # represent the current folder
Path("demo_packaging/__init__.py")
Path() / Path("demo_packaging")
Path() / "demo_packaging" / "__init__.py"
print(Path.home())  # return current user home

init_file_path = Path("demo_packaging/__init__.py")
package_path = Path("demo_packaging")

if init_file_path.exists():
    print(f"{init_file_path.name} exists")
    print(f"{init_file_path.name} is file: {init_file_path.is_file()}")
    print(f"{init_file_path.name} is directory: {init_file_path.is_dir()}")
    if init_file_path.is_file():
        print(init_file_path.name)
        print(init_file_path.stem)
        print(init_file_path.suffix)
        print(init_file_path.parent)
        print(init_file_path.absolute())

if package_path.exists():
    print(f"{package_path.name} exists")
    print(f"{package_path.name} is file: {package_path.is_file()}")
    print(f"{package_path.name} is directory: {package_path.is_dir()}")


# Create a new path from existing path with new file name.
sample_txt_file_path = init_file_path.with_name("sample.txt")
print("sample_txt_file_path:", sample_txt_file_path.absolute())

# Create a new path from existing path with new file extension.
init_txt_file_path = init_file_path.with_suffix(".txt")
print("init_txt_file_path:", init_txt_file_path.absolute())