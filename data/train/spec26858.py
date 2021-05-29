import numpy as np 

def function(x):

	a9 = 4
	c0 = 1
	paths = []
	try:
		if c0 < 8:
			a9 = c0/a9
			c0 = c0*5
			a9 = x-a9
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if x < 3:
			x = 3+x
			a9 = 1/a9
			x = x/6
			paths.append(3)
		else:
			x = c0*x
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))