# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"AD5..00","system":"readv2"},{"code":"AD50.00","system":"readv2"},{"code":"AD53.00","system":"readv2"},{"code":"AD53000","system":"readv2"},{"code":"AD54.00","system":"readv2"},{"code":"AD55.00","system":"readv2"},{"code":"Cyu0600","system":"readv2"},{"code":"F013.00","system":"readv2"},{"code":"F326300","system":"readv2"},{"code":"F374900","system":"readv2"},{"code":"F396500","system":"readv2"},{"code":"G558300","system":"readv2"},{"code":"G5y7.00","system":"readv2"},{"code":"H57y200","system":"readv2"},{"code":"J63A.00","system":"readv2"},{"code":"N233200","system":"readv2"},{"code":"26405.0","system":"med"},{"code":"27769.0","system":"med"},{"code":"28952.0","system":"med"},{"code":"33980.0","system":"med"},{"code":"34437.0","system":"med"},{"code":"3859.0","system":"med"},{"code":"3865.0","system":"med"},{"code":"40613.0","system":"med"},{"code":"40751.0","system":"med"},{"code":"47037.0","system":"med"},{"code":"47718.0","system":"med"},{"code":"49075.0","system":"med"},{"code":"49454.0","system":"med"},{"code":"52519.0","system":"med"},{"code":"55612.0","system":"med"},{"code":"58841.0","system":"med"},{"code":"72595.0","system":"med"},{"code":"73284.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('sarcoidosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["sarcoidosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["sarcoidosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["sarcoidosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
