'''
Script removes unicode and rejoins words back into a string
'''

import re
import csv
import sys

text = "0,\"REPORTS FROM RURAL CENTRES MONTAC[?] His Excellency the Governor (Sir Malcolm Barclay-Harvey) paid an informal visit to the Montacute public school. His Excellency was accompanied by Lady Muriel and Hiss Rose-Mary Llddell-Oraineer. Mr. C Oepp iflcoined them on behalf ol the school and welfare club committees., uule Norm* Whelaa : presented Lady Muriel ?:ta * sbeaf of ro=e?. *nd Nfil Ross presented His Excellency with * basket ol fruit from the boys and tirl.? o! the school. The Governor addressed the children end granted them * day's holiday. "

def remove_regex(input_text):
	clean_text = re.compile(r'\W+', re.UNICODE).split(input_text)
	return(" ".join( clean_text ))

print(remove_regex(text))