import numpy as np 

def function(x):

	c9 = 2
	l8 = x
	paths = []
	try:
		if l8 > 2:
			x = x*6
			c9 = 2-4
			l8 = x/1
			paths.append(1)
		else:
			l8 = l8/c9
			x = x-4
			x = l8+x
			paths.append(2)
		if l8 <= 9:
			x = x/7
			paths.append(3)
		else:
			l8 = l8+4
			x = x/9
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))