import numpy as np 

def function(x):

	c7 = x
	y2 = x
	paths = []
	try:
		if y2 <= 6:
			x = 3/x
			c7 = 2*2
			c7 = c7-8
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if y2 < 9:
			x = 5/5
			c7 = 7/2
			paths.append(3)
		else:
			y2 = y2*9
			c7 = x*0
			x = 4-8
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