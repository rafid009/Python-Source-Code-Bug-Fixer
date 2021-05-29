import numpy as np 

def function(x):

	i0 = x
	c8 = x
	paths = []
	try:
		if c8 >= 4:
			x = c8/x
			paths.append(1)
		else:
			i0 = 1+i0
			c8 = 1+c8
			x = x/c8
			paths.append(2)
		if i0 <= 3:
			x = x+i0
			x = 6/x
			paths.append(3)
		else:
			c8 = 9*c8
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		i0 = c8**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))