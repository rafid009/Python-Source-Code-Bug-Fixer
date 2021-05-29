import numpy as np 

def function(x):

	e6 = 5
	k6 = 8
	paths = []
	try:
		if k6 <= 5:
			k6 = 1*9
			paths.append(1)
		else:
			e6 = 0*e6
			paths.append(2)
		if e6 > 6:
			k6 = k6*7
			paths.append(3)
		else:
			x = x*6
			x = 1-x
			e6 = e6*e6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))