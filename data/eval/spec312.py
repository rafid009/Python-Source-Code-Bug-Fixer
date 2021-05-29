import numpy as np 

def function(x):

	n4 = x
	b5 = 1
	paths = []
	try:
		if x >= 4:
			x = 1/x
			paths.append(1)
		else:
			n4 = n4+4
			paths.append(2)
		if n4 < 6:
			b5 = 7+b5
			x = x-b5
			b5 = b5+4
			paths.append(3)
		else:
			x = 6*x
			n4 = b5+x
			b5 = b5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))