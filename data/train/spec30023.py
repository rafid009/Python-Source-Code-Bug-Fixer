import numpy as np 

def function(x):

	n8 = x
	l9 = 1
	paths = []
	try:
		if x >= 7:
			n8 = 7*l9
			paths.append(1)
		else:
			x = 0-9
			x = n8+n8
			paths.append(2)
		if l9 < 9:
			n8 = 4-n8
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))