import numpy as np 

def function(x):

	l6 = x
	u0 = x
	paths = []
	try:
		if x <= 1:
			l6 = l6/7
			u0 = u0-9
			x = 4*x
			paths.append(1)
		else:
			u0 = x-3
			u0 = l6/3
			paths.append(2)
		if x > 3:
			x = 6*8
			x = x+7
			paths.append(3)
		else:
			x = 9+x
			l6 = l6+l6
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		l6 = u0**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))