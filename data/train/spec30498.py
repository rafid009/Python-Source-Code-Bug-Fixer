import numpy as np 

def function(x):

	c9 = x
	b3 = x
	paths = []
	try:
		if b3 < 9:
			c9 = c9-4
			paths.append(1)
		else:
			b3 = b3+9
			paths.append(2)
		if c9 < 6:
			c9 = b3*9
			c9 = c9/2
			paths.append(3)
		else:
			b3 = 8-9
			c9 = c9*b3
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		b3 = c9**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))