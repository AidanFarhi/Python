from sys import argv
from csv import reader

def main():
    # First check if the right amount of command line args were given
    if len(argv) != 3:
        print('Usage: python dna.py <filename>.csv <filename>.txt')

    # Store file names
    csv_filename = argv[1]
    txt_filename = argv[2]

    # Load data from csv file
    strs = []  # Store STR's in a list
    names_and_values = []  # Store the names and values in an list
    load_csv_data(csv_filename, strs, names_and_values)

    # Load data from txt file and store in a string
    sequence = load_txt_data(txt_filename)

    # Now count subsequent STR sequences in the sequence string and store in a list
    counts = [0] * len(strs)
    get_str_counts(strs, counts, sequence)

    # Print result
    print_result(names_and_values, counts)


def load_csv_data(filename, strs, names_and_values):
    # Open csv file and read each row
    with open(filename) as csv_file:
        rows = reader(csv_file)
        for row in rows:
            if row[0] == 'name':  # First row of csv
                for i in range(1, len(row)):  # Load each STR into a set
                    strs.append(row[i])
            else:
                names_and_values.append(row)


def load_txt_data(filename):
    sequence = ''
    # Open txt file and store content as a string
    with open(filename) as txt_file:
        sequence = txt_file.read().replace('\n', '')
    return sequence


def get_str_counts(strs, counts, sequence):
    for i, STR in enumerate(strs):
        n = len(STR)
        for j in range(len(sequence)):
            if j + n == len(sequence):
                break
            if sequence[j:j+n] == STR:
                current = 0
                for k in range(j, len(sequence), n):
                    if k + n == len(sequence):
                        break
                    if sequence[k:k+n] == STR:
                        current += 1
                    else:
                        break
                if current > int(counts[i]):
                    counts[i] = str(current)


def print_result(names_and_values, counts):
    result = 'No match'
    for row in names_and_values:
        if row[1:] == counts:
            result = row[0]
    print(result)


main()