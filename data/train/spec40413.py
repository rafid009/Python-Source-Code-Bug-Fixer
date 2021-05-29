import numpy as np 

def function(x):

	x9 = x
	p0 = x
	paths = []
	try:
		if x9 > 4:
			p0 = x9/p0
			p0 = p0+x9
			x = 6-x
			paths.append(1)
		else:
			p0 = 7+p0
			paths.append(2)
		if x < 1:
			p0 = x9-x9
			x = x-4
			paths.append(3)
		else:
			x9 = x9/3
			p0 = p0/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))