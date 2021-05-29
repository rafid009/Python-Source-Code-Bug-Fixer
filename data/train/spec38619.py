import numpy as np 

def function(x):

	x5 = x
	c2 = x
	paths = []
	try:
		if c2 > 7:
			c2 = c2-9
			c2 = c2*c2
			paths.append(1)
		else:
			x5 = 9-4
			paths.append(2)
		if c2 <= 8:
			x = 4-1
			x5 = 2/x5
			x = 0/x
			paths.append(3)
		else:
			x5 = c2+c2
			x5 = 1/x5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))