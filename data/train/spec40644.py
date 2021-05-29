import numpy as np 

def function(x):

	g3 = x
	c8 = x
	x = 9
	paths = []
	try:
		if x < 3:
			x = x+c8
			paths.append(1)
		else:
			c8 = c8+4
			c8 = c8-4
			x = x*c8
			paths.append(2)
		if c8 > 4:
			g3 = 3-7
			paths.append(3)
		else:
			x = 6*c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))