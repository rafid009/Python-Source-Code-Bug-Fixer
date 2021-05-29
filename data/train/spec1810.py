import numpy as np 

def function(x):

	d0 = 6
	r3 = x
	paths = []
	try:
		if r3 > 7:
			r3 = r3/x
			x = x+0
			paths.append(1)
		else:
			x = 2/x
			r3 = 6*r3
			x = 3+x
			paths.append(2)
		if r3 > 7:
			x = 8+x
			d0 = r3*6
			x = x/r3
			paths.append(3)
		else:
			x = r3*7
			d0 = d0+r3
			d0 = d0*7
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