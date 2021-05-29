import numpy as np 

def function(x):

	c5 = x
	y7 = x
	paths = []
	try:
		if c5 > 5:
			y7 = 1+9
			c5 = c5-6
			paths.append(1)
		else:
			x = x*1
			c5 = c5*c5
			paths.append(2)
		if y7 > 8:
			x = x-c5
			x = x*c5
			y7 = x*x
			paths.append(3)
		else:
			y7 = 9/c5
			y7 = x/y7
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))