import numpy as np 

def function(x):

	c9 = x
	a4 = 0
	x = x
	paths = []
	try:
		if c9 <= 5:
			a4 = 9-a4
			paths.append(1)
		else:
			x = x/c9
			x = x*9
			c9 = c9/2
			paths.append(2)
		if a4 > 2:
			c9 = 9*c9
			x = x-9
			paths.append(3)
		else:
			x = 8/x
			a4 = a4+x
			c9 = a4/a4
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))