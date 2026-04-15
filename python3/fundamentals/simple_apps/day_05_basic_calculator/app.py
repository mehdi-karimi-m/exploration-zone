import platform
import sys
import tty
import termios


def windows_get_char():
    return None


def linux_get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)  # raw mode: no Enter needed
        ch = sys.stdin.read(1)  # read one character
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def get_char():
    if platform.system() == "Windows":
        # print("Running on Windows")
        return windows_get_char()
    elif platform.system() == "Linux":
        # print("Running on Linux")
        return linux_get_char()
    elif platform.system() == "Darwin":
        # print("Running on macOS")
        return None


def is_valid_command(command):
    return command == "+" or command == "-" or command == "/" or command == "*"


def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    return 0


memory = 0
number = ""
is_continue = True
last_command = "="
while is_continue:
    char = get_char()
    sys.stdout.write(char)
    sys.stdout.flush()

    if char == "*":
        if number.isdecimal():
            memory = float(number)
        number = ""
        last_command = "*"
    elif char == "/":
        if number.isdecimal():
            memory = float(number)
        number = ""
        last_command = "/"
    elif char == "+":
        if number.isdecimal():
            memory = float(number)
        number = ""
        last_command = "+"
    elif char == "-":
        if number.isdecimal():
            memory = float(number)
        number = ""
        last_command = "-"
    elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        if char == "." and (not "." in number):
            number += char
        elif char != ".":
            number += char
    elif char == "\r":
        if is_valid_command(last_command):
            if number.isdecimal():
                num = float(number)
                result = calculate(memory, last_command, num)
                print(f"{memory} {last_command} {num} = {result}")
            memory = 0
            number = ""
            last_command = ""
    else:
        is_continue = False
