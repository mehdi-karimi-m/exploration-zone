from pprint import pprint
from pathlib import Path

print(("=" * 10) + " Working by directories " + ("=" * 10))
my_directory = Path() / "my_directory"
if not my_directory.exists():
    print("my_directory.exists():", my_directory.exists())
    print("my_directory.mkdir()", my_directory.mkdir())
    print("my_directory.rename(""my_directory2"")")
    my_directory = my_directory.rename("my_directory2")
    print("my_directory.rmdir()", my_directory.rmdir())

print("----- iterdir() -----")
home_directory = Path.home()
for path in home_directory.iterdir():
    print(path)

print("*" * 20)

paths = [p for p in home_directory.iterdir() if p.is_file()]
pprint(paths)

# glob return search result in folder
print("****************** Path.glob() ******************")
all_txt_files_in_folder = [p for p in home_directory.glob("*.txt")]
pprint(all_txt_files_in_folder)

print("****************** Path.rglob() ******************")
# rglob return recursive search result
all_txt_files_in_folder_and_its_subfolders = [
    p for p in home_directory.rglob("*.txt")] #rglob("*.txt") == glob("**/*.txt")
pprint(all_txt_files_in_folder_and_its_subfolders)