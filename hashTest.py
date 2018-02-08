import random
import time
hashTable = [[]]*10000
array = [None]*10000

def hashFunc(x):
	hashIndex = x%10000
	#print x,
	#print " mod ",
	#print " 100000 = " + str(hashIndex)
	return hashIndex

def hashSearch(table, x, value):
	i=0
	while 1==1:
		if(table[x] == value):
			print "Found: ",
			print x
			break

def contains(x):
	global array
	for i in range(len(array)):
		if(array[i] == x):
			return i
		

def main():
	global array
	global hashTable
	
	for x in range(len(array)):
  		number = random.randint(1,10001)	
		array[x] = number

	
	print "HASH TABLE: ",
	print hashTable
	print "ARRAY: ",
	print array
	
	for i in range(len(array)):
		index = hashFunc(array[i])
		hashTable[index] = array[i]
	#	print hashTable

	value = input('Enter a number: ')

	start_time_hash = time.time()
	searchIndex = hashFunc(value)
	print "\nHASH SEARCH"
	print hashSearch(hashTable, searchIndex, value)
	print "--- %s seconds ---" % ((time.time() - start_time_hash))
	
	start_time_array = time.time()
	print "\nARRAY SEARCH"
	print contains(value)
	print "--- %s seconds ---" % ((time.time() - start_time_array))


if __name__ == '__main__': main()	
