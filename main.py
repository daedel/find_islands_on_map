import sys

from src.map_reader.count_islands import count_islands

if __name__ == '__main__':
    stdin_args = sys.argv[1:]
    if len(stdin_args) != 2:
        print(
            "You have to pass 2 parameters: latitude and longitude. Example command to run script python main.py 19.261833190918 -155.393173217773"
        )
        exit(0)

    count_islands()