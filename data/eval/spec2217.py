import numpy as np 

def function(x):

	b8 = 3
	c9 = 8
	x = x
	paths = []
	try:
		if x < 4:
			c9 = 4*c9
			paths.append(1)
		else:
			b8 = 8*b8
			paths.append(2)
		if c9 < 2:
			x = 8-8
			paths.append(3)
		else:
			x = x-x
			x = x+5
			c9 = 8-c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		b8 = c9**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))