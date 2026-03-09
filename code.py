import os
import re
import argparse

def search(pattern, path, ignore_case=False):
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags)
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, 1):
                        if regex.search(line):
                            print(f"{file_path}:{i}:{line.rstrip()}")
            except:
                pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    parser.add_argument("path")
    parser.add_argument("-i", "--ignore-case", action="store_true")
    args = parser.parse_args()
    search(args.pattern, args.path, args.ignore_case)

if __name__ == "__main__":
    main()
