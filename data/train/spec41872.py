import numpy as np 

def function(x):

	c5 = 4
	b6 = 5
	paths = []
	try:
		if b6 > 7:
			b6 = b6-b6
			paths.append(1)
		else:
			b6 = 1+b6
			paths.append(2)
		if c5 > 2:
			b6 = b6-x
			c5 = 1-c5
			c5 = c5/2
			paths.append(3)
		else:
			x = x-b6
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))