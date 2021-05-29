import numpy as np 

def function(x):

	v9 = 5
	e6 = x
	paths = []
	try:
		if v9 <= 0:
			e6 = 7/e6
			x = x-e6
			paths.append(1)
		else:
			v9 = 8-v9
			x = 5/x
			v9 = 2/v9
			paths.append(2)
		if e6 < 7:
			x = v9*x
			e6 = e6-3
			paths.append(3)
		else:
			e6 = 0*x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))