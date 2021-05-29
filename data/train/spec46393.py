import numpy as np 

def function(x):

	e2 = 5
	l7 = x
	paths = []
	try:
		if x < 1:
			l7 = x+l7
			paths.append(1)
		else:
			e2 = 1*e2
			paths.append(2)
		if e2 >= 6:
			l7 = l7/6
			e2 = 4-e2
			paths.append(3)
		else:
			x = e2+l7
			l7 = l7+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))