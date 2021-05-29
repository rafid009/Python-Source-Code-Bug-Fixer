import numpy as np 

def function(x):

	l6 = 3
	e8 = x
	paths = []
	try:
		if e8 <= 5:
			l6 = 3-l6
			e8 = e8*x
			l6 = l6/4
			paths.append(1)
		else:
			x = l6+l6
			e8 = e8+l6
			e8 = 0+e8
			paths.append(2)
		if x >= 9:
			l6 = l6/2
			e8 = e8-l6
			paths.append(3)
		else:
			e8 = e8+2
			e8 = 0/3
			x = l6-x
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