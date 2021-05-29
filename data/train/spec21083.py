import numpy as np 

def function(x):

	q6 = 3
	u0 = 1
	paths = []
	try:
		if u0 <= 3:
			x = x-8
			u0 = 9/u0
			paths.append(1)
		else:
			u0 = u0*2
			x = x*x
			paths.append(2)
		if x < 7:
			q6 = 5*q6
			u0 = x/3
			x = u0*2
			paths.append(3)
		else:
			x = x*2
			x = 1-6
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