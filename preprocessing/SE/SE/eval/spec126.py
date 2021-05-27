import numpy as np 

def function(x):

	c9 = x
	a6 = x
	paths = []
	try:
		if a6 >= 3:
			c9 = 7*c9
			paths.append(1)
		else:
			c9 = c9*1
			a6 = 6-a6
			c9 = c9/8
			paths.append(2)
		if a6 > 8:
			x = 9*x
			paths.append(3)
		else:
			a6 = 5+a6
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