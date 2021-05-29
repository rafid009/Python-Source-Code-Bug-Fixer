import numpy as np 

def function(x):

	l0 = x
	l4 = 2
	paths = []
	try:
		if l4 < 2:
			l0 = 1*l4
			x = l0/x
			l0 = 0-0
			paths.append(1)
		else:
			l4 = 5/5
			paths.append(2)
		if l4 >= 6:
			x = l4-2
			paths.append(3)
		else:
			l0 = l4/l0
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