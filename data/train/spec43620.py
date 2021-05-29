import numpy as np 

def function(x):

	o6 = 5
	q6 = 0
	paths = []
	try:
		if q6 <= 6:
			q6 = q6*3
			o6 = 3*o6
			paths.append(1)
		else:
			x = 4*9
			paths.append(2)
		if q6 >= 2:
			x = 1/x
			q6 = q6*5
			paths.append(3)
		else:
			x = x*o6
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