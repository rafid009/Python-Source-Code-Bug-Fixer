import numpy as np 

def function(x):

	p7 = 1
	x5 = 2
	paths = []
	try:
		if x >= 7:
			x5 = x+x5
			p7 = 8-x5
			x = 7+8
			paths.append(1)
		else:
			x5 = 4+x5
			p7 = 4*p7
			paths.append(2)
		if x <= 6:
			p7 = 7+8
			p7 = x5-p7
			x = 3-2
			paths.append(3)
		else:
			x = 1-x
			x = x+p7
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