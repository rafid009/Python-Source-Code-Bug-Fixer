import numpy as np 

def function(x):

	j9 = 2
	c2 = 6
	paths = []
	try:
		if j9 > 2:
			c2 = c2-j9
			c2 = j9*2
			c2 = 1*7
			paths.append(1)
		else:
			j9 = x/9
			j9 = j9*4
			x = j9+j9
			paths.append(2)
		if x >= 8:
			c2 = 5/c2
			c2 = x+3
			paths.append(3)
		else:
			c2 = 9-j9
			c2 = c2/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))