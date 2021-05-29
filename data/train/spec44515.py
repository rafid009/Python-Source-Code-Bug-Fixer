import numpy as np 

def function(x):

	n0 = 6
	b9 = 8
	paths = []
	try:
		if b9 >= 4:
			n0 = 4+1
			n0 = 0-n0
			paths.append(1)
		else:
			b9 = b9*b9
			b9 = b9+8
			paths.append(2)
		if b9 <= 2:
			b9 = b9-b9
			b9 = 3+b9
			paths.append(3)
		else:
			n0 = n0*n0
			b9 = 4*b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))