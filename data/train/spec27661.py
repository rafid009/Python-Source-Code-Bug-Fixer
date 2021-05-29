import numpy as np 

def function(x):

	l4 = x
	e4 = 5
	paths = []
	try:
		if x <= 2:
			x = x/1
			l4 = l4/4
			x = x-x
			paths.append(1)
		else:
			l4 = 4*l4
			e4 = 9*l4
			l4 = 1-x
			paths.append(2)
		if e4 < 9:
			x = x/3
			paths.append(3)
		else:
			l4 = 0+4
			e4 = x*6
			x = x/5
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		e4 = l4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))