import numpy as np 

def function(x):

	n2 = x
	n4 = 6
	paths = []
	try:
		if x < 5:
			n2 = 3+x
			n4 = x-n2
			paths.append(1)
		else:
			x = x-6
			x = x+x
			x = 3*2
			paths.append(2)
		if n4 < 1:
			n4 = 8*n4
			paths.append(3)
		else:
			n4 = n4/2
			n2 = 4+n2
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))