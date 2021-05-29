import numpy as np 

def function(x):

	c5 = 7
	a0 = x
	x = 0
	paths = []
	try:
		if x <= 4:
			x = x+3
			a0 = 7*a0
			paths.append(1)
		else:
			a0 = a0/a0
			paths.append(2)
		if c5 < 8:
			c5 = 8*3
			x = 6/x
			paths.append(3)
		else:
			c5 = 0-9
			a0 = a0-a0
			c5 = c5*c5
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))