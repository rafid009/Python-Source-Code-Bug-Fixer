import numpy as np 

def function(x):

	p8 = 9
	v2 = x
	paths = []
	try:
		if p8 < 9:
			p8 = 5/p8
			v2 = v2*v2
			x = x-0
			paths.append(1)
		else:
			v2 = x-6
			paths.append(2)
		if p8 < 4:
			p8 = 0+2
			p8 = 0-5
			x = 1-x
			paths.append(3)
		else:
			v2 = 5*v2
			p8 = x+p8
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