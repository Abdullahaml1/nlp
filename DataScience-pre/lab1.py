'''
This is the first lab in the DS course
Data: http://users.umiacs.umd.edu/~jbg/teaching/INST_414/2012pres.csv
lab link: http://users.umiacs.umd.edu/~jbg/teaching/INST_414/lab01.pdf
'''
from csv import DictReader

votes = list(DictReader(open("2012pres.csv", 'r'),  delimiter=";"))




