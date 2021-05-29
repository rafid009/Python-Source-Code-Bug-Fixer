import numpy as np 

def function(x):

	c7 = 9
	b7 = x
	x = x
	paths = []
	try:
		if x < 2:
			x = x-b7
			c7 = c7*x
			c7 = c7*3
			paths.append(1)
		else:
			b7 = x+b7
			paths.append(2)
		if x < 9:
			x = x-b7
			x = x-7
			paths.append(3)
		else:
			x = x*0
			b7 = b7+b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))