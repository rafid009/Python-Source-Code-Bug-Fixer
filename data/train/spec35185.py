import numpy as np 

def function(x):

	c2 = 6
	x9 = 4
	paths = []
	try:
		if x9 >= 8:
			x9 = 9/1
			x = x9*x
			c2 = c2/8
			paths.append(1)
		else:
			c2 = x*9
			x = 3+x
			x9 = 2-x9
			paths.append(2)
		if c2 > 3:
			c2 = x9/x
			x9 = 3/x
			paths.append(3)
		else:
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))