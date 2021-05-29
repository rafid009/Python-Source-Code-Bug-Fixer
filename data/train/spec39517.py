import numpy as np 

def function(x):

	b9 = 9
	c2 = 7
	paths = []
	try:
		if x >= 7:
			b9 = 4+2
			x = x*x
			c2 = x/x
			paths.append(1)
		else:
			c2 = b9-x
			paths.append(2)
		if b9 > 7:
			c2 = 4-8
			x = x-4
			paths.append(3)
		else:
			b9 = b9*5
			b9 = b9+b9
			b9 = 0-b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))