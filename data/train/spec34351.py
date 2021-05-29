import numpy as np 

def function(x):

	v4 = 5
	e5 = x
	paths = []
	try:
		if x <= 6:
			v4 = 4-1
			e5 = 8-e5
			e5 = 1*1
			paths.append(1)
		else:
			v4 = 2/v4
			x = 4*x
			paths.append(2)
		if v4 < 9:
			v4 = v4*v4
			v4 = v4/3
			e5 = e5*v4
			paths.append(3)
		else:
			e5 = e5+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))