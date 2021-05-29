import numpy as np 

def function(x):

	l7 = x
	c1 = x
	paths = []
	try:
		if x >= 4:
			x = 0+l7
			l7 = 9-6
			x = 2-6
			paths.append(1)
		else:
			l7 = c1+1
			l7 = x/4
			paths.append(2)
		if c1 > 7:
			l7 = l7-c1
			x = x/l7
			c1 = c1*c1
			paths.append(3)
		else:
			l7 = 1-l7
			l7 = 9/3
			x = 3-5
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))