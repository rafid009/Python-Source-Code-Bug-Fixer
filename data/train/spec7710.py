import numpy as np 

def function(x):

	c5 = 8
	l7 = x
	paths = []
	try:
		if l7 > 0:
			x = 2/c5
			l7 = c5/l7
			paths.append(1)
		else:
			c5 = c5+4
			c5 = x-c5
			paths.append(2)
		if l7 <= 8:
			l7 = l7*c5
			x = l7/x
			c5 = c5*1
			paths.append(3)
		else:
			x = x*5
			x = 7*x
			c5 = 6-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))