import numpy as np 

def function(x):

	n8 = x
	l2 = 2
	paths = []
	try:
		if l2 <= 9:
			n8 = 4/n8
			x = 2/4
			paths.append(1)
		else:
			l2 = 1-6
			paths.append(2)
		if l2 <= 6:
			l2 = 4+4
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))