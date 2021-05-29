import numpy as np 

def function(x):

	p0 = x
	c3 = 8
	paths = []
	try:
		if p0 > 8:
			x = x+c3
			paths.append(1)
		else:
			c3 = 5-c3
			p0 = 3-p0
			paths.append(2)
		if x <= 1:
			c3 = 2-c3
			paths.append(3)
		else:
			x = 3*x
			x = 5*c3
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