import numpy as np 

def function(x):

	k4 = x
	c7 = x
	paths = []
	try:
		if c7 > 6:
			k4 = k4*k4
			c7 = c7-c7
			paths.append(1)
		else:
			k4 = 5*k4
			k4 = c7*9
			c7 = c7+c7
			paths.append(2)
		if x < 4:
			c7 = c7+c7
			c7 = c7+6
			x = 0+x
			paths.append(3)
		else:
			x = 0-x
			x = 4/8
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		k4 = c7**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))