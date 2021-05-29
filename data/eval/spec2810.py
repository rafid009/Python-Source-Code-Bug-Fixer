import numpy as np 

def function(x):

	c2 = 6
	l0 = 4
	paths = []
	try:
		if x >= 4:
			x = x+x
			paths.append(1)
		else:
			c2 = x-c2
			l0 = 5*l0
			paths.append(2)
		if x > 2:
			x = 2+0
			paths.append(3)
		else:
			l0 = l0*5
			x = x+l0
			l0 = 0+c2
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))