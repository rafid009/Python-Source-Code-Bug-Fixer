import numpy as np 

def function(x):

	c2 = 6
	z9 = x
	paths = []
	try:
		if x <= 3:
			c2 = 3-c2
			c2 = c2-7
			x = x-5
			paths.append(1)
		else:
			x = 1-0
			paths.append(2)
		if z9 > 0:
			c2 = c2/x
			paths.append(3)
		else:
			x = 5-c2
			x = x+5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		z9 = c2**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))