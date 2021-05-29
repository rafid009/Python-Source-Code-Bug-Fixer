import numpy as np 

def function(x):

	b3 = x
	n6 = 0
	paths = []
	try:
		if b3 < 2:
			n6 = 0/b3
			x = 5-7
			paths.append(1)
		else:
			b3 = b3+7
			paths.append(2)
		if n6 > 2:
			n6 = n6*5
			paths.append(3)
		else:
			b3 = b3*n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))