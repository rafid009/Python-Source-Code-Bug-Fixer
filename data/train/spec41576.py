import numpy as np 

def function(x):

	e5 = 4
	v3 = 2
	paths = []
	try:
		if x <= 4:
			e5 = x/7
			e5 = v3*x
			paths.append(1)
		else:
			v3 = 5+4
			paths.append(2)
		if x >= 0:
			v3 = e5/4
			paths.append(3)
		else:
			v3 = 7/v3
			v3 = v3/x
			v3 = v3/e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))