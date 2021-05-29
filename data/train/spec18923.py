import numpy as np 

def function(x):

	d9 = x
	g0 = 8
	x = x
	paths = []
	try:
		if g0 <= 6:
			g0 = x+g0
			x = 8-x
			x = x/1
			paths.append(1)
		else:
			g0 = d9+x
			paths.append(2)
		if d9 > 3:
			d9 = 8+6
			x = g0*x
			paths.append(3)
		else:
			d9 = 5+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))