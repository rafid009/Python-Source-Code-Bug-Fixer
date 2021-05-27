import numpy as np 

def function(x):

	k4 = 5
	n1 = x
	x = 3
	paths = []
	try:
		if n1 >= 9:
			k4 = 5/k4
			x = x-4
			paths.append(1)
		else:
			k4 = k4*n1
			n1 = 1/3
			paths.append(2)
		if n1 > 7:
			n1 = n1/k4
			paths.append(3)
		else:
			n1 = 8-9
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		n1 = k4**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))