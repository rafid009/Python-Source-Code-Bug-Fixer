import numpy as np 

def function(x):

	n1 = x
	c4 = 8
	paths = []
	try:
		if n1 < 6:
			x = x/1
			c4 = 1*2
			paths.append(1)
		else:
			x = x-5
			c4 = 3*c4
			c4 = 5/n1
			paths.append(2)
		if n1 >= 1:
			x = 5-5
			n1 = n1*c4
			paths.append(3)
		else:
			c4 = 4+x
			c4 = 8*x
			c4 = 8/c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))