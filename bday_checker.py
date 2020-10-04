#Birthday reminder application




def writing():
	fh = open('bday.txt','a')
	data = input("Format: Date(dd/mm/yyyy)<space>Name\n")
	fh.write(data)
	fh.write('\n')
	fh.close()

def check():
	fh = open('bday.txt','r')
	date = input('Date:(Format: dd/mm/yyyy)\n')
	count = 0
	for line in fh:
		dates = line.rstrip().split()
		dd = dates[0]
		if(date == dd):
			print(dates[1])
			count = count +1
		dates.clear()
	if(count == 0):
		print('Not Found!')



def switchcase(oper):
	if oper == '1':
		writing()
	elif oper == '2':
		check()
	elif oper == '3':
		quit()	




#fh = open('bday.txt')	

while(True):
	print('Function List (Choose any):\n 1. Add a date\n 2. Check a date \n 3. Exit\n')
	oper = input()
	switchcase(oper)
