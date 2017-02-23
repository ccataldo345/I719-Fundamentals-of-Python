# in command prompt> python FileReader.py wordlist.txt;

import argparse

def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()
    text_file = open(args.file_name)
    for line in text_file:
        print(line.strip())
    text_file.close()

if __name__ == '__main__':
    main()


