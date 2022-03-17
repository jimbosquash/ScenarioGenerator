import csv

class Logger:

    def createCSV(name):
        filename = name + "Test.csv"
        with open(filename, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Name', 'Profession'])
            filewriter.writerows([['Name', 'Profession'],['Derek', 'Software Developer'],['Steve', 'Software Developer']])
            #filewriter.writerow(['Derek', 'Software Developer'])
            #filewriter.writerow(['Steve', 'Software Developer'])
            #filewriter.writerow(['Paul', 'Manager'])

    def createCSV(name,array):
        filename = name + ".csv"
        with open(filename, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for entry in array:
                filewriter.writerow(entry)

    def openFile(name):
        fileName = name + '.csv'
        with open(fileName, 'r') as f:
            reader = csv.reader(f)
            # read file row by row
            for row in reader:
                print (row)