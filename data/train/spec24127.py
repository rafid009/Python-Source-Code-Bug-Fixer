import numpy as np 

def function(x):

	a0 = x
	c9 = 8
	paths = []
	try:
		if c9 <= 2:
			c9 = c9-9
			x = 2+x
			x = 7-4
			paths.append(1)
		else:
			a0 = x+a0
			a0 = a0/a0
			paths.append(2)
		if a0 < 4:
			a0 = x*2
			x = x-x
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		c9 = a0**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))