import numpy as np 

def function(x):

	c3 = 8
	l4 = x
	paths = []
	try:
		if x <= 6:
			c3 = 8/l4
			paths.append(1)
		else:
			x = 2-l4
			paths.append(2)
		if l4 < 6:
			x = 1*1
			l4 = l4*6
			paths.append(3)
		else:
			l4 = x/l4
			l4 = l4*2
			x = c3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))