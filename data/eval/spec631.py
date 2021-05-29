import numpy as np 

def function(x):

	j3 = x
	c2 = 5
	paths = []
	try:
		if j3 < 4:
			j3 = 2+0
			x = x*c2
			paths.append(1)
		else:
			j3 = j3*j3
			j3 = 0+j3
			c2 = j3+0
			paths.append(2)
		if x >= 9:
			x = 1-x
			c2 = 2*6
			paths.append(3)
		else:
			j3 = 5/6
			c2 = j3*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))