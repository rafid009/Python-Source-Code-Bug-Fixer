import numpy as np 

def function(x):

	u5 = 9
	q1 = 4
	paths = []
	try:
		if q1 < 6:
			u5 = u5+3
			u5 = 4*q1
			x = x-1
			paths.append(1)
		else:
			x = x*9
			u5 = 9/3
			paths.append(2)
		if q1 > 2:
			u5 = 1*u5
			q1 = u5/q1
			paths.append(3)
		else:
			q1 = 8+x
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