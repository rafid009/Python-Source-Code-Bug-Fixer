import numpy as np 

def function(x):

	l0 = x
	n3 = 6
	paths = []
	try:
		if x <= 5:
			l0 = l0-7
			paths.append(1)
		else:
			x = 1*5
			paths.append(2)
		if x < 4:
			n3 = n3*5
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))