import getopt
import sys
from file_parser import parse_file


def main(argv):
    input_files = []
    help_text = 'main.py -i <input_file>'
    try:
        opts, args = getopt.getopt(argv, "h:i:", ["ifile="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit()
    if len(opts) < 1:
        print(help_text)
        sys.exit()
    for opt, arg in opts:
        if opt == "-h":
            print(help_text)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_files.append(arg)
    if len(input_files) > 0:
        for file in input_files:
            print("Opening file" + file)
            parse_file(file)
    else:
        print(help_text)
        sys.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
