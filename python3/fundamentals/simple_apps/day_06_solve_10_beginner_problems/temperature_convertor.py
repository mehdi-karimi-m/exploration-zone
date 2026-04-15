def cilicious_to_firenhight(cili):
    return cili * 1.4

def firenhight_to_cilicious(firen):
    return firen / 1.4

print("1- cilicious to firenhight")
print("2- firenhight to cilicious")
print("3- exit")

command = input()

while command == "1" or command == "2":
    if(command == "1"):
        cilicious = int(input("Enter cilicious: "))
        print(f"{cilicious} is {cilicious_to_firenhight(cilicious)} firenhight.")
    
    if command == "2":
        firen = int(input("Enter firenhight: "))
        print(f"{firen} is {firenhight_to_cilicious(firen)} cilicious.")

    print("1- cilicious to firenhight")
    print("2- firenhight to cilicious")
    print("3- exit")
    command = input()
