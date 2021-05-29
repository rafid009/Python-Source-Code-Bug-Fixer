import numpy as np 

def function(x):

	a0 = x
	c1 = 6
	x = 4
	paths = []
	try:
		if a0 >= 5:
			c1 = x*4
			paths.append(1)
		else:
			x = x-3
			c1 = c1-9
			a0 = 2*a0
			paths.append(2)
		if a0 < 5:
			a0 = a0-c1
			c1 = c1*3
			a0 = a0+0
			paths.append(3)
		else:
			c1 = c1+8
			x = x*9
			c1 = 3*x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))