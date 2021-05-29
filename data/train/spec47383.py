import numpy as np 

def function(x):

	l7 = x
	e3 = 6
	x = x
	paths = []
	try:
		if x <= 0:
			e3 = e3+4
			paths.append(1)
		else:
			l7 = l7-l7
			paths.append(2)
		if l7 >= 3:
			e3 = e3/x
			l7 = 1/1
			paths.append(3)
		else:
			l7 = l7+l7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))