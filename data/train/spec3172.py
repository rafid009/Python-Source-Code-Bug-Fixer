import numpy as np 

def function(x):

	l2 = x
	u0 = 2
	paths = []
	try:
		if l2 > 1:
			u0 = x*u0
			paths.append(1)
		else:
			l2 = 6*x
			u0 = u0/u0
			u0 = l2+u0
			paths.append(2)
		if u0 > 9:
			x = x-x
			l2 = 5*6
			l2 = l2*1
			paths.append(3)
		else:
			u0 = u0-u0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))