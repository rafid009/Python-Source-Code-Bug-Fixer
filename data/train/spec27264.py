import numpy as np 

def function(x):

	p5 = x
	c2 = 3
	paths = []
	try:
		if c2 <= 6:
			c2 = 0-c2
			paths.append(1)
		else:
			c2 = 8-1
			x = 0+7
			paths.append(2)
		if x < 7:
			c2 = c2-x
			paths.append(3)
		else:
			c2 = 0-1
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