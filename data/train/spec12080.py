import numpy as np 

def function(x):

	i6 = x
	c6 = x
	paths = []
	try:
		if i6 >= 8:
			c6 = i6/i6
			c6 = x/i6
			x = c6-i6
			paths.append(1)
		else:
			x = 9+x
			i6 = 9-i6
			paths.append(2)
		if x <= 7:
			c6 = c6*6
			i6 = 4-i6
			paths.append(3)
		else:
			c6 = 7*4
			c6 = 5+5
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))