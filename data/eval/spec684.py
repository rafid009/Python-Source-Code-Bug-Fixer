import numpy as np 

def function(x):

	e2 = x
	l0 = 6
	paths = []
	try:
		if x < 8:
			l0 = 9/9
			paths.append(1)
		else:
			x = 6/x
			x = l0*x
			l0 = 5*9
			paths.append(2)
		if x <= 4:
			l0 = e2+l0
			paths.append(3)
		else:
			e2 = e2/7
			x = l0/6
			l0 = l0+l0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))