import numpy as np 

def function(x):

	j8 = 2
	c6 = x
	paths = []
	try:
		if x >= 0:
			c6 = 3+7
			c6 = c6*0
			j8 = j8-3
			paths.append(1)
		else:
			j8 = 1/6
			x = j8/5
			paths.append(2)
		if c6 < 3:
			j8 = 5/2
			c6 = x+c6
			paths.append(3)
		else:
			c6 = 3/3
			x = x+5
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))