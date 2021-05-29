import numpy as np 

def function(x):

	l4 = x
	n4 = x
	paths = []
	try:
		if l4 <= 8:
			n4 = 5*n4
			n4 = x*1
			x = 7/x
			paths.append(1)
		else:
			x = l4/2
			paths.append(2)
		if n4 >= 3:
			x = x+5
			paths.append(3)
		else:
			n4 = 4+n4
			x = x*7
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