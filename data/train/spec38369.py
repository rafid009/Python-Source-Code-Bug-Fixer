import numpy as np 

def function(x):

	l0 = 5
	a4 = 7
	x = x
	paths = []
	try:
		if a4 < 0:
			x = 7+x
			paths.append(1)
		else:
			a4 = a4+x
			x = x/2
			l0 = l0/a4
			paths.append(2)
		if x >= 1:
			x = x/x
			a4 = x-a4
			paths.append(3)
		else:
			x = a4+x
			a4 = l0-2
			a4 = l0-a4
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