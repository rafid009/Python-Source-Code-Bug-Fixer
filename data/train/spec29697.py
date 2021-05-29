import numpy as np 

def function(x):

	l4 = x
	c2 = 9
	paths = []
	try:
		if l4 <= 3:
			c2 = 0*1
			c2 = c2-6
			paths.append(1)
		else:
			c2 = 0+l4
			paths.append(2)
		if l4 >= 0:
			c2 = 8+c2
			l4 = 7/l4
			paths.append(3)
		else:
			l4 = c2-l4
			c2 = c2-x
			c2 = 5/c2
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