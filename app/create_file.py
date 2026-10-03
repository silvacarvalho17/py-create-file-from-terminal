import os
import sys
from datetime import datetime


def get_content() -> str:
    lines = []
    counter = 1

    while True:
        text = input("Enter content line: ")

        if text == "stop":
            break

        lines.append(f"{counter} {text}")
        counter += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return timestamp + "\n" + "\n".join(lines)


def main() -> None:
    args = sys.argv[1:]

    directory_path = ""
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")
            dirs = args[d_index + 1:f_index]
        else:
            dirs = args[d_index + 1:]

        directory_path = os.path.join(*dirs)

        os.makedirs(directory_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

        content = get_content()

        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        mode = "a" if os.path.exists(file_path) else "w"

        with open(file_path, mode) as file:
            if mode == "a":
                file.write("\n\n")
            file.write(content)


if __name__ == "__main__":
    main()
