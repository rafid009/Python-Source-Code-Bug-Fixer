import numpy as np 

def function(x):

	a2 = x
	c4 = x
	x = 8
	paths = []
	try:
		if a2 < 1:
			a2 = a2+6
			x = 7+1
			paths.append(1)
		else:
			c4 = a2*c4
			a2 = a2*a2
			x = 1/1
			paths.append(2)
		if a2 >= 4:
			x = 5+x
			c4 = 8/c4
			c4 = c4-5
			paths.append(3)
		else:
			x = x*3
			c4 = 5+c4
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		c4 = a2**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))