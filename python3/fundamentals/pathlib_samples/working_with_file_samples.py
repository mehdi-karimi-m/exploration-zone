from pathlib import Path
from time import ctime
from pprint import pprint
import shutil

# We can use Path class to crud files like this:
current_path = Path(__file__)

path = current_path.with_name("hello_world.txt")
print(path)
print("exists:", path.exists())
if path.exists():
    path.unlink()

path.write_text("Hello World!")
print(path.absolute())
print(path.read_text())
pprint(path.stat())
print(ctime(path.stat().st_ctime))

my_file_path = path.with_name("my_file.txt")
if my_file_path.exists():
    my_file_path.unlink()
my_file = path.rename(my_file_path)
print(path.absolute())
print(my_file.absolute())

print("****************** Reading file by open() ******************")
with open(my_file, "r") as file:
    for line in file.readlines():
        print(line)

source = my_file
target = my_file.with_name("copy_of_my_file.txt")
if target.exists():
    target.unlink()

#target.write_bytes(source.read_bytes())
shutil.copy(source, target) #this is better way than target.write_bytes(...)