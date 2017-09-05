import sys
import nltk
import csv
nltk.download('punkt')

REFERENCE_FILE = "test_input.csv"
ref_f= open(REFERENCE_FILE)
reference_reader = csv.reader(ref_f)
next(reference_reader)    

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout)
header = next(reader)
writer.writerow(header)
for row in reader:
    bigrams_row = set(nltk.bigrams([w for w in nltk.word_tokenize(row[1])
                                    if ',' not in w and '"' not in w
                                       and ' ' not in w]))
    ref_row = next(reference_reader)
    bigrams_ref = set(nltk.bigrams([w for w in nltk.word_tokenize(ref_row[1])
                                    if ',' not in w and '"' not in w
                                       and ' ' not in w]))
    row[1] = " ".join(['_'.join(b) for b in bigrams_row - bigrams_ref])
    writer.writerow(row)
