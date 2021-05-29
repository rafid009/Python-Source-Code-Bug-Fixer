import numpy as np 

def function(x):

	c7 = x
	c2 = 2
	paths = []
	try:
		if c7 > 9:
			x = 4/7
			paths.append(1)
		else:
			c2 = 3*2
			paths.append(2)
		if c7 < 7:
			c2 = 8/c7
			x = 1-8
			paths.append(3)
		else:
			x = x/1
			x = x*3
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