import numpy as np 

def function(x):

	a0 = 0
	l4 = x
	paths = []
	try:
		if x < 4:
			a0 = 6/5
			a0 = 3/a0
			paths.append(1)
		else:
			x = 5-l4
			a0 = a0-l4
			paths.append(2)
		if x <= 0:
			l4 = l4/l4
			l4 = 5+l4
			l4 = 4+l4
			paths.append(3)
		else:
			l4 = a0*2
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		a0 = l4**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))