import numpy as np 

def function(x):

	x7 = x
	c6 = 7
	paths = []
	try:
		if x > 6:
			c6 = 7*c6
			x = 9+x
			x7 = x7*x
			paths.append(1)
		else:
			x = 7*c6
			x7 = x7/9
			paths.append(2)
		if x <= 4:
			x = x+2
			c6 = 2+c6
			paths.append(3)
		else:
			c6 = c6+9
			x = 0+7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))