import numpy as np 

def function(x):

	c6 = x
	l8 = x
	paths = []
	try:
		if x <= 7:
			x = x+c6
			l8 = 0+l8
			l8 = 3-l8
			paths.append(1)
		else:
			x = l8+x
			l8 = x/l8
			paths.append(2)
		if c6 >= 3:
			x = 2+8
			l8 = l8-1
			l8 = 7-x
			paths.append(3)
		else:
			x = x*3
			c6 = x+c6
			x = c6-l8
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))