import numpy as np 

def function(x):

	l1 = 1
	c6 = x
	x = 8
	paths = []
	try:
		if c6 < 1:
			l1 = 0-c6
			paths.append(1)
		else:
			c6 = l1*9
			l1 = c6+1
			c6 = c6-c6
			paths.append(2)
		if l1 > 9:
			x = c6*1
			x = 3+l1
			c6 = 9+c6
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))