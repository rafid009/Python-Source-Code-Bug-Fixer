import numpy as np 

def function(x):

	c2 = 8
	r0 = 5
	paths = []
	try:
		if c2 <= 8:
			r0 = r0/3
			c2 = r0*4
			paths.append(1)
		else:
			c2 = c2+5
			paths.append(2)
		if x <= 4:
			r0 = x-2
			x = x+8
			x = 9-x
			paths.append(3)
		else:
			c2 = c2/c2
			c2 = c2*8
			x = x*r0
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