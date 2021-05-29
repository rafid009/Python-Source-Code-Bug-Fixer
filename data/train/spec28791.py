import numpy as np 

def function(x):

	u0 = 4
	l6 = 1
	paths = []
	try:
		if l6 < 6:
			l6 = 9+x
			paths.append(1)
		else:
			u0 = 6/u0
			paths.append(2)
		if u0 > 4:
			x = x-l6
			x = 6/x
			l6 = l6+l6
			paths.append(3)
		else:
			u0 = u0*u0
			u0 = 3/5
			u0 = u0+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))