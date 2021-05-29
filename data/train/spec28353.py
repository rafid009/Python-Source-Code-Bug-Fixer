import numpy as np 

def function(x):

	v0 = x
	p8 = x
	paths = []
	try:
		if x > 7:
			v0 = v0-4
			x = p8-x
			x = v0+x
			paths.append(1)
		else:
			x = x-6
			p8 = p8+6
			paths.append(2)
		if p8 < 6:
			p8 = p8/x
			x = x*x
			paths.append(3)
		else:
			p8 = 7/p8
			p8 = 9+x
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