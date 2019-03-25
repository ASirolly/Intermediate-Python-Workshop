import csv
import string
import sys
import time

# Consants
INPUT = str(sys.argv[1])
OUTPUT = str(sys.argv[2])

def isNum(num_string):
    try:
        float(num_string)
        return True
    except ValueError:
        return False

def parse(line):
    data_dict = dict()
    if line[0] in string.ascii_letters:
        line = line.lower().replace(" ", "").strip("\n").split(',')
        for entry in line:
            if ":" in entry:
                data = entry.split(':')
                if data[0].isalpha() and isNum(data[1]):
                    data_dict[data[0]] = float(data[1])
    if len(data_dict) != 0:
        return data_dict

def main():
    data_dicts = list()

    with open(INPUT, "r") as fp:
        for line in fp:
            line = parse(line)
            if line is not None:
                data_dicts.append(line)
        print(data_dicts)


    with open(OUTPUT, "w") as fp:
        writer = csv.DictWriter(fp, data_dicts[0].keys())
        writer.writeheader()
        writer.writerows(data_dicts)

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed = time.time() - start
    elapsed_min = elapsed // 60
    elapsed_sec = elapsed % 60
    print("program ran in {} minutes and {:.5f} seconds".format(elapsed_min, elapsed_sec))
