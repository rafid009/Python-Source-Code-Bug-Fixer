import numpy as np 

def function(x):

	c7 = x
	r2 = 2
	paths = []
	try:
		if x <= 6:
			c7 = 3+7
			c7 = 9+9
			c7 = c7*1
			paths.append(1)
		else:
			c7 = c7/8
			r2 = r2*6
			paths.append(2)
		if x < 1:
			r2 = r2/x
			r2 = r2*2
			paths.append(3)
		else:
			r2 = r2-0
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