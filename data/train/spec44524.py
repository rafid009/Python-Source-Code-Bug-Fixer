import numpy as np 

def function(x):

	e3 = x
	k6 = x
	paths = []
	try:
		if k6 > 2:
			e3 = e3-e3
			k6 = k6-1
			paths.append(1)
		else:
			k6 = x*7
			paths.append(2)
		if x <= 1:
			e3 = 6*3
			e3 = 1+e3
			paths.append(3)
		else:
			e3 = e3-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))