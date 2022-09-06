import csv
import os

def jarkomdat():
    ip = []
    site = []
    y = 2
    z = 0
    number = input('Masukkan Kode Site Daerah: ')

    csv_file = csv.reader(open('masterdata.csv', 'r'), delimiter=",")

    for row in csv_file:

            if number == row[0]:
                    while y <= 5:
                            ip.append(str(row[y]))
                            y = y+1
            
                    while z <= 1:
                            site.append(str(row[z]))
                            z = z+1

    choose = input('[0] PING \n[1] PING Beban\n[0 or 1]: ')
    os.system('cls')
    print ('Sistem PING Bekerja untuk site : ')
    print (site)

    if choose == '0':
		          for x in ip:
    			         rep = os.system('ping ' + x)
    			         print ('-----------------------------------------------------------')
    elif choose == '1':
		          for x in ip:
				            rep = os.system('ping ' + x + ' -l 1472')
				            print ('-----------------------------------------------------------')
    else:
	       print ('not found')
    os.system('pause')
    os.system('cls')
while True:
    jarkomdat()
