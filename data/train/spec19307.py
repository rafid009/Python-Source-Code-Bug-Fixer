import numpy as np 

def function(x):

	l2 = 8
	c6 = 0
	paths = []
	try:
		if c6 <= 2:
			x = x*2
			x = x-l2
			l2 = l2*1
			paths.append(1)
		else:
			x = 1*x
			c6 = c6+x
			l2 = l2/l2
			paths.append(2)
		if c6 > 7:
			c6 = 6+7
			c6 = x-9
			paths.append(3)
		else:
			c6 = 5-l2
			c6 = 4/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))