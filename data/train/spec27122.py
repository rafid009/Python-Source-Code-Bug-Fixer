import numpy as np 

def function(x):

	c6 = x
	g9 = x
	paths = []
	try:
		if g9 <= 9:
			c6 = c6/5
			paths.append(1)
		else:
			x = x-g9
			paths.append(2)
		if x >= 9:
			g9 = x*1
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))