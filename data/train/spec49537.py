import numpy as np 

def function(x):

	p0 = x
	a8 = 8
	paths = []
	try:
		if p0 < 7:
			x = x*p0
			paths.append(1)
		else:
			p0 = x*p0
			x = x-9
			paths.append(2)
		if x < 1:
			x = 8-x
			p0 = 2/p0
			paths.append(3)
		else:
			a8 = 1+2
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		x = p0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))