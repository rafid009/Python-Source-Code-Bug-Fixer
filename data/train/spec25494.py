import numpy as np 

def function(x):

	u0 = 1
	y3 = x
	paths = []
	try:
		if y3 <= 1:
			y3 = 2/y3
			x = x-5
			y3 = y3*y3
			paths.append(1)
		else:
			u0 = u0/y3
			u0 = 9/u0
			u0 = 6/u0
			paths.append(2)
		if x <= 9:
			y3 = y3*1
			x = x*4
			u0 = u0+u0
			paths.append(3)
		else:
			u0 = u0+1
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