import numpy as np 

def function(x):

	k6 = 4
	e6 = 8
	paths = []
	try:
		if k6 <= 5:
			e6 = e6*7
			e6 = k6+7
			e6 = 2*k6
			paths.append(1)
		else:
			k6 = e6+k6
			paths.append(2)
		if x < 1:
			k6 = 7-x
			x = x*9
			paths.append(3)
		else:
			k6 = 7/k6
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