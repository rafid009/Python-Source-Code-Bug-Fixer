import numpy as np 

def function(x):

	y5 = x
	c4 = 3
	paths = []
	try:
		if x > 7:
			y5 = 3/y5
			y5 = 1/x
			paths.append(1)
		else:
			c4 = c4-7
			paths.append(2)
		if y5 >= 8:
			c4 = 1*0
			c4 = x+3
			c4 = 5+c4
			paths.append(3)
		else:
			y5 = y5-c4
			y5 = y5/x
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		y5 = c4**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))