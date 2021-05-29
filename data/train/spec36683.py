import numpy as np 

def function(x):

	l7 = 6
	c5 = 1
	paths = []
	try:
		if c5 >= 5:
			c5 = 0*1
			x = c5/x
			c5 = c5/c5
			paths.append(1)
		else:
			l7 = 0+l7
			x = 7*x
			c5 = c5-1
			paths.append(2)
		if x < 3:
			c5 = l7+x
			x = x+1
			paths.append(3)
		else:
			l7 = 6*l7
			c5 = 6*x
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