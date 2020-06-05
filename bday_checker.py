#Birthday reminder application

def writing():
	fh = open('bday.txt','a')
	data = input("Format: Date(dd/mm/yyyy)<space>Name\n")
	fh.write(data + "\n")
	fh.close()

def check():
	fh = open('bday.txt','r')
	date = input('Date: (Format: dd/mm/yyyy)\n')
	for line in fh:
		dates = line.rstrip().split()
		if dates[0] == date:
			print(dates[1])
		else:
			print('Not found!')


def switchcase(oper):
	if oper == '1':
		writing()
	elif oper == '2':
		check()
	elif oper == '3':
		quit()	




#fh = open('bday.txt')	

while(True):
	print('What op to perform:\n 1. Add a date\n 2. Check a date \n 3. Exit\n')
	oper = input()
	switchcase(oper)
