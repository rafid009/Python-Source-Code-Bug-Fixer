import numpy as np 

def function(x):

	q6 = x
	u2 = 6
	paths = []
	try:
		if u2 > 2:
			u2 = 7*u2
			paths.append(1)
		else:
			x = x*x
			q6 = 0*x
			q6 = x*3
			paths.append(2)
		if q6 < 5:
			q6 = q6/u2
			paths.append(3)
		else:
			u2 = 6-4
			q6 = 5*4
			u2 = 0/u2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))