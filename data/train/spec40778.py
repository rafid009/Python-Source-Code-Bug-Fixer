import numpy as np 

def function(x):

	d4 = x
	p8 = 8
	paths = []
	try:
		if p8 < 1:
			p8 = 3-p8
			paths.append(1)
		else:
			d4 = d4*d4
			paths.append(2)
		if d4 <= 6:
			x = 4*x
			p8 = 7-x
			paths.append(3)
		else:
			p8 = 4*p8
			d4 = 0+d4
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