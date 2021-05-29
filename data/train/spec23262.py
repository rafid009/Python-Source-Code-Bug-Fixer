import numpy as np 

def function(x):

	c2 = x
	x8 = 1
	x = 6
	paths = []
	try:
		if x < 7:
			c2 = x8-4
			paths.append(1)
		else:
			x8 = c2-0
			x = x/3
			paths.append(2)
		if x >= 2:
			c2 = 4*c2
			c2 = c2+4
			x8 = x8/x
			paths.append(3)
		else:
			x8 = x8/3
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x8 = c2**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))