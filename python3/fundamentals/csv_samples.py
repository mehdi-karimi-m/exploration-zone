from pathlib import Path
import csv

csv_file_path = Path("data.csv")
if csv_file_path.exists():
    csv_file_path.unlink()

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["first_name", "last_name", "age"])
    writer.writerow(["Mehdi", "Karimi", 43])
    writer.writerow(["Mina", "Taheri", 37])

with open("data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
