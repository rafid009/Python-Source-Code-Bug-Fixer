import numpy as np 

def function(x):

	l8 = 0
	c2 = 6
	paths = []
	try:
		if x > 5:
			l8 = 0+l8
			paths.append(1)
		else:
			l8 = x/c2
			paths.append(2)
		if x < 1:
			l8 = l8/3
			x = x*1
			paths.append(3)
		else:
			l8 = c2/x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))