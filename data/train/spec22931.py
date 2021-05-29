import numpy as np 

def function(x):

	b3 = x
	c2 = 9
	paths = []
	try:
		if c2 <= 3:
			c2 = c2-0
			paths.append(1)
		else:
			b3 = b3/6
			paths.append(2)
		if b3 >= 6:
			b3 = 5-b3
			paths.append(3)
		else:
			c2 = c2+4
			x = x+7
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