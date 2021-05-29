import numpy as np 

def function(x):

	l2 = x
	c4 = x
	x = x
	paths = []
	try:
		if l2 >= 4:
			c4 = 9/c4
			c4 = 8*8
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x >= 1:
			x = x*c4
			paths.append(3)
		else:
			x = 7+x
			l2 = 6/l2
			l2 = l2*x
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