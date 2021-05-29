import numpy as np 

def function(x):

	a8 = 6
	l4 = x
	paths = []
	try:
		if l4 < 6:
			l4 = l4-x
			paths.append(1)
		else:
			x = a8-x
			paths.append(2)
		if a8 <= 9:
			l4 = l4-7
			paths.append(3)
		else:
			x = l4+x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		a8 = l4**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))