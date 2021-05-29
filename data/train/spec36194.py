import numpy as np 

def function(x):

	l4 = x
	a9 = x
	paths = []
	try:
		if x <= 4:
			l4 = 5/x
			a9 = a9-x
			paths.append(1)
		else:
			l4 = 1*l4
			paths.append(2)
		if x >= 1:
			l4 = a9/9
			paths.append(3)
		else:
			l4 = l4*8
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