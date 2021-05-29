import numpy as np 

def function(x):

	c2 = x
	l9 = 4
	x = 7
	paths = []
	try:
		if c2 <= 9:
			c2 = x+7
			paths.append(1)
		else:
			x = x-3
			c2 = 9/c2
			x = 1/2
			paths.append(2)
		if l9 <= 8:
			l9 = l9-x
			c2 = 2*l9
			paths.append(3)
		else:
			c2 = 2+c2
			l9 = 1-4
			c2 = 6+c2
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))