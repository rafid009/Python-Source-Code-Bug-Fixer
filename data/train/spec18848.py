import numpy as np 

def function(x):

	b9 = 7
	c6 = 9
	paths = []
	try:
		if c6 < 9:
			c6 = 0-7
			b9 = b9-3
			b9 = c6/b9
			paths.append(1)
		else:
			c6 = c6+2
			x = x*6
			b9 = b9/6
			paths.append(2)
		if x < 4:
			x = x-2
			c6 = 5/c6
			c6 = c6*4
			paths.append(3)
		else:
			c6 = 2-c6
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