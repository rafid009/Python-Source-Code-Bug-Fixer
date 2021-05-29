import numpy as np 

def function(x):

	c6 = 4
	k1 = x
	paths = []
	try:
		if x > 2:
			c6 = 6-2
			x = c6-x
			paths.append(1)
		else:
			c6 = c6/x
			c6 = c6*3
			c6 = 9+c6
			paths.append(2)
		if x >= 4:
			x = x+c6
			c6 = 7*3
			paths.append(3)
		else:
			c6 = 4*4
			c6 = c6*9
			c6 = x*0
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))