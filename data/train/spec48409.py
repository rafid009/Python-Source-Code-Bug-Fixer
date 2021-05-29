import numpy as np 

def function(x):

	l6 = 4
	e0 = x
	paths = []
	try:
		if e0 >= 1:
			x = 2+l6
			x = x*3
			paths.append(1)
		else:
			e0 = e0+e0
			paths.append(2)
		if x < 3:
			l6 = l6+8
			paths.append(3)
		else:
			l6 = l6-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))