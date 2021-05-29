import numpy as np 

def function(x):

	i9 = 7
	c5 = x
	paths = []
	try:
		if i9 > 0:
			i9 = i9+c5
			x = 9/i9
			paths.append(1)
		else:
			i9 = i9*8
			i9 = 3/i9
			i9 = i9/1
			paths.append(2)
		if c5 > 0:
			x = 1*x
			x = 1/x
			i9 = 4*5
			paths.append(3)
		else:
			x = 2/x
			i9 = 7*i9
			x = x/x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))