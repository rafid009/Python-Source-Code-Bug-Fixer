import numpy as np 

def function(x):

	c1 = 8
	x2 = x
	paths = []
	try:
		if x2 >= 5:
			c1 = c1*8
			x2 = x2*x2
			paths.append(1)
		else:
			c1 = c1/3
			x = x*c1
			c1 = c1-c1
			paths.append(2)
		if c1 < 6:
			c1 = c1*x2
			c1 = 4+x2
			paths.append(3)
		else:
			x2 = x2-6
			x = 8*2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))