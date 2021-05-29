import numpy as np 

def function(x):

	c0 = 2
	l1 = 5
	paths = []
	try:
		if x <= 7:
			x = l1+x
			c0 = l1/2
			c0 = c0-l1
			paths.append(1)
		else:
			l1 = 3-0
			l1 = 9/2
			paths.append(2)
		if l1 < 1:
			l1 = l1*4
			paths.append(3)
		else:
			l1 = x*1
			c0 = c0-c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))