import numpy as np 

def function(x):

	e8 = x
	k6 = 0
	x = x
	paths = []
	try:
		if x >= 6:
			x = 8+k6
			k6 = x*k6
			paths.append(1)
		else:
			e8 = x-1
			k6 = 5+4
			paths.append(2)
		if x < 3:
			k6 = k6*x
			e8 = 0/x
			paths.append(3)
		else:
			e8 = e8+k6
			k6 = k6/9
			k6 = k6-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))