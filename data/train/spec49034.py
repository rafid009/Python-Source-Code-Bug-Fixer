import numpy as np 

def function(x):

	c1 = x
	a6 = 6
	x = 2
	paths = []
	try:
		if x >= 6:
			c1 = 0-c1
			x = 1-x
			x = x-x
			paths.append(1)
		else:
			x = 0+x
			c1 = 2-5
			paths.append(2)
		if x < 6:
			a6 = a6+a6
			a6 = a6-1
			a6 = 4*5
			paths.append(3)
		else:
			x = x*a6
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		a6 = c1**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))