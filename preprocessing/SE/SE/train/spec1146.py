import numpy as np 

def function(x):

	l6 = 4
	e7 = x
	paths = []
	try:
		if e7 < 2:
			e7 = e7-3
			paths.append(1)
		else:
			x = 2/8
			paths.append(2)
		if l6 <= 3:
			e7 = e7+e7
			x = 5+x
			x = e7/x
			paths.append(3)
		else:
			l6 = l6+x
			x = l6/9
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