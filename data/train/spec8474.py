import numpy as np 

def function(x):

	i7 = x
	c3 = 3
	x = 2
	paths = []
	try:
		if i7 > 2:
			c3 = c3+x
			paths.append(1)
		else:
			x = 8/c3
			c3 = c3/6
			paths.append(2)
		if i7 > 4:
			i7 = c3-i7
			i7 = i7+9
			x = x*6
			paths.append(3)
		else:
			x = x-6
			c3 = 3-i7
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))