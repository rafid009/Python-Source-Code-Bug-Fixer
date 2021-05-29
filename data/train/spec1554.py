import numpy as np 

def function(x):

	a1 = 8
	c6 = 9
	paths = []
	try:
		if a1 > 4:
			a1 = x*a1
			x = x*3
			a1 = a1*4
			paths.append(1)
		else:
			c6 = c6-c6
			a1 = 2*1
			paths.append(2)
		if c6 < 7:
			a1 = 1/6
			paths.append(3)
		else:
			c6 = x+a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))