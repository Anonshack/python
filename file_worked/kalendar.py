import csv

with open("clay.txt") as clay:
      csv_reader = csv.reader(clay, delimiter=',');
      for row in csv_reader:
            if row[0] == 'id':
                  continue;
            print(f'{row[0]}-oy {row[1]}, unda {row[2]} kun bor');