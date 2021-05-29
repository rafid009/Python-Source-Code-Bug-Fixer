import numpy as np 

def function(x):

	v7 = x
	c4 = 9
	paths = []
	try:
		if v7 >= 3:
			c4 = 9*c4
			paths.append(1)
		else:
			x = x*2
			c4 = 0+c4
			paths.append(2)
		if v7 <= 5:
			x = 7-c4
			v7 = 9+6
			c4 = 1-c4
			paths.append(3)
		else:
			v7 = 7/1
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))