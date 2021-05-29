import numpy as np 

def function(x):

	m8 = x
	n7 = x
	paths = []
	try:
		if x <= 2:
			x = x+4
			n7 = n7-1
			paths.append(1)
		else:
			x = x-4
			n7 = m8-n7
			n7 = x-4
			paths.append(2)
		if x < 4:
			m8 = 0*8
			x = m8-6
			n7 = n7-1
			paths.append(3)
		else:
			m8 = x-x
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))