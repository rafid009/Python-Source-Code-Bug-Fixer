import numpy as np 

def function(x):

	c9 = x
	b5 = 0
	paths = []
	try:
		if b5 < 3:
			c9 = c9*6
			b5 = b5+b5
			paths.append(1)
		else:
			x = 9-1
			b5 = x-b5
			paths.append(2)
		if b5 >= 8:
			x = x/x
			paths.append(3)
		else:
			c9 = c9/6
			x = 7*x
			b5 = x-3
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))