import numpy as np 

def function(x):

	i0 = 3
	n1 = 2
	paths = []
	try:
		if x >= 6:
			n1 = 1*5
			x = 9-x
			i0 = i0-9
			paths.append(1)
		else:
			i0 = i0*7
			paths.append(2)
		if n1 < 0:
			n1 = n1-4
			n1 = i0/n1
			paths.append(3)
		else:
			n1 = 0*n1
			x = x/5
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		n1 = i0**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))