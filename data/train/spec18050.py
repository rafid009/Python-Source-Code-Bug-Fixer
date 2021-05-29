import numpy as np 

def function(x):

	y5 = 1
	c5 = x
	paths = []
	try:
		if y5 < 4:
			y5 = 2-7
			y5 = y5-3
			c5 = c5+4
			paths.append(1)
		else:
			x = 2/x
			x = 2/x
			x = x/y5
			paths.append(2)
		if y5 > 2:
			y5 = c5*7
			x = 3+c5
			c5 = c5-6
			paths.append(3)
		else:
			y5 = 5*2
			c5 = c5/4
			y5 = y5*2
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		y5 = c5**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))