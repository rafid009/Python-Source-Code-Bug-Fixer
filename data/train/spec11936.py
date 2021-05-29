import numpy as np 

def function(x):

	a5 = 2
	l4 = x
	paths = []
	try:
		if a5 >= 6:
			a5 = a5*4
			a5 = 2*a5
			paths.append(1)
		else:
			l4 = 3-8
			a5 = l4+3
			l4 = 0-l4
			paths.append(2)
		if a5 > 3:
			x = x/a5
			x = x+l4
			x = 9-a5
			paths.append(3)
		else:
			l4 = l4/8
			x = 8/8
			l4 = l4+a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))