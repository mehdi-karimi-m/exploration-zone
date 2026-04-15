from zipfile import ZipFile
from pathlib import Path

home = Path.home()
zip_directory = home / "Pictures"
print(home)
zip_file_path = home / "home-zipped.zip"
with ZipFile(zip_file_path, "w", allowZip64=True) as zip:
    for f in zip_directory.rglob("*.*"):
        if f.exists():
            print(f"{f} - file/directory added")
            zip.write(f)

print("*" * 30)

with ZipFile(zip_file_path, "r") as zip_file:
    for file_name in zip_file.namelist():
        print(file_name)
        file_info = zip_file.getinfo(file_name)
        # print("file_info.compress_level:", file_info.compress_level)
        print("file_info.compress_size:", file_info.compress_size)
        print("file_info.file_size:", file_info.file_size)
        print("file_info.compress_type:", file_info.compress_type)
        print("file_info.create_system:", file_info.create_system)
        print("file_info.create_version:", file_info.create_version)
        print("file_info.date_time:", file_info.date_time)
    temp_directory = home / "temp"
    if not temp_directory.exists():
        temp_directory.mkdir()
        zip_file.extractall(temp_directory)
