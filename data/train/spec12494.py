import numpy as np 

def function(x):

	q4 = 4
	n4 = 1
	paths = []
	try:
		if q4 < 7:
			n4 = 1+q4
			n4 = n4/1
			paths.append(1)
		else:
			x = x+4
			n4 = n4+4
			n4 = n4*1
			paths.append(2)
		if q4 > 5:
			x = n4+x
			x = x+6
			paths.append(3)
		else:
			q4 = 9*q4
			n4 = x+5
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))