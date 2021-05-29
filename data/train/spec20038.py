import numpy as np 

def function(x):

	c7 = 7
	a7 = 6
	paths = []
	try:
		if a7 >= 9:
			a7 = a7/2
			c7 = c7*a7
			paths.append(1)
		else:
			c7 = a7+4
			c7 = 1+c7
			paths.append(2)
		if a7 >= 0:
			a7 = 1-a7
			paths.append(3)
		else:
			c7 = 0*0
			a7 = 8-5
			c7 = x+a7
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