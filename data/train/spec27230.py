import numpy as np 

def function(x):

	c7 = x
	n2 = 6
	paths = []
	try:
		if n2 <= 4:
			x = x-x
			paths.append(1)
		else:
			c7 = n2*8
			paths.append(2)
		if x >= 2:
			c7 = 7*7
			paths.append(3)
		else:
			c7 = 8-4
			c7 = n2*1
			c7 = c7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))