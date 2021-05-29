import numpy as np 

def function(x):

	l9 = x
	c9 = 7
	paths = []
	try:
		if x > 9:
			c9 = c9-0
			c9 = c9/5
			x = 5/7
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if c9 >= 7:
			x = x-c9
			c9 = c9/3
			paths.append(3)
		else:
			l9 = x/1
			x = x/x
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