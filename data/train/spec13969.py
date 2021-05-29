import numpy as np 

def function(x):

	c8 = 5
	r2 = x
	paths = []
	try:
		if r2 >= 0:
			c8 = x/r2
			r2 = r2-9
			paths.append(1)
		else:
			x = x/r2
			r2 = r2+6
			x = x-r2
			paths.append(2)
		if r2 > 5:
			x = 0+x
			r2 = 3-8
			paths.append(3)
		else:
			x = x+3
			x = c8+2
			r2 = r2*r2
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))