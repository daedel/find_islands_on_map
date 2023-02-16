import sys

from map_reader.count_islands import count_islands

if __name__ == "__main__":
    stdin_args = sys.argv[1:]
    if len(stdin_args) != 1:
        print("You have to pass exactly 1 parameter: path_to_file")
        exit(0)
    print(count_islands(stdin_args[0]))
