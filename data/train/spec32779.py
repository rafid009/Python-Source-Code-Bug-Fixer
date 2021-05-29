import numpy as np 

def function(x):

	a8 = 9
	l8 = 4
	paths = []
	try:
		if a8 < 3:
			x = 1*a8
			a8 = 1/a8
			a8 = 4-a8
			paths.append(1)
		else:
			l8 = x-l8
			x = x/x
			paths.append(2)
		if x <= 6:
			l8 = x*l8
			a8 = a8-8
			x = x-4
			paths.append(3)
		else:
			l8 = 6+l8
			x = a8*x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		a8 = l8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))