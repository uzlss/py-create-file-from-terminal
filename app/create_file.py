import datetime
import sys
import os


def create_file(path: str) -> None:
    with open(path, "a") as file:
        line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        index = 0

        while line != "stop":
            if index:
                line = f"{index} {line}"

            file.write(line + "\n")
            line = input("Enter content line: ")
            index += 1

        file.write("\n")


def read_line() -> None:
    line_args = sys.argv[1:]
    path = []

    if "-d" in line_args:
        dirs = line_args[line_args.index("-d") + 1:]  # DRY?
        for index, arg in enumerate(dirs):
            if arg == "-f":
                line_args = line_args[index + 1:]
                break
            path.append(arg)

        os.makedirs(os.path.join(*path), exist_ok=True)

    if "-f" in line_args:
        create_file(os.path.join(*path, line_args[1]))


if __name__ == "__main__":
    read_line()
