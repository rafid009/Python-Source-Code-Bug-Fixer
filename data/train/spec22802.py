import numpy as np 

def function(x):

	c3 = 0
	a3 = x
	paths = []
	try:
		if a3 < 4:
			c3 = c3-9
			a3 = a3*9
			a3 = 3*x
			paths.append(1)
		else:
			c3 = c3-8
			paths.append(2)
		if x <= 6:
			c3 = c3*9
			c3 = c3-1
			x = a3*3
			paths.append(3)
		else:
			c3 = c3*x
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))