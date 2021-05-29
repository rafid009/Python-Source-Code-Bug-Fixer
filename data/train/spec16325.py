import numpy as np 

def function(x):

	n1 = x
	l8 = 6
	paths = []
	try:
		if x >= 8:
			x = x*8
			paths.append(1)
		else:
			l8 = l8+7
			l8 = l8/6
			l8 = 2+l8
			paths.append(2)
		if x > 9:
			n1 = 0/n1
			n1 = 1*n1
			paths.append(3)
		else:
			n1 = 2/8
			n1 = 0-l8
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))