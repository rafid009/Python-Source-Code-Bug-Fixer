import numpy as np 

def function(x):

	u7 = 0
	c9 = x
	x = 2
	paths = []
	try:
		if u7 < 8:
			c9 = 0+c9
			x = 3-x
			x = 0-x
			paths.append(1)
		else:
			c9 = c9/3
			paths.append(2)
		if x > 0:
			u7 = u7-x
			paths.append(3)
		else:
			x = x+2
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