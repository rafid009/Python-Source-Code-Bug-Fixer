import numpy as np 

def function(x):

	q6 = x
	r3 = x
	paths = []
	try:
		if q6 <= 9:
			x = x/r3
			r3 = r3/r3
			paths.append(1)
		else:
			q6 = 5-q6
			x = 7/2
			q6 = 2*9
			paths.append(2)
		if q6 >= 9:
			x = x*q6
			r3 = 3+r3
			x = q6-r3
			paths.append(3)
		else:
			r3 = 3-r3
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