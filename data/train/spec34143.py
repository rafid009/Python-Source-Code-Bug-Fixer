import numpy as np 

def function(x):

	e8 = x
	c6 = 0
	x = 6
	paths = []
	try:
		if x > 1:
			c6 = c6/7
			paths.append(1)
		else:
			x = 1-x
			e8 = e8/1
			c6 = x*c6
			paths.append(2)
		if c6 < 1:
			x = 8+x
			c6 = c6+9
			c6 = 4+0
			paths.append(3)
		else:
			x = 2+e8
			e8 = x/e8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))