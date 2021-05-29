import numpy as np 

def function(x):

	v4 = x
	e3 = 5
	paths = []
	try:
		if x > 8:
			e3 = 0/5
			paths.append(1)
		else:
			v4 = 0*9
			e3 = e3+7
			v4 = v4/x
			paths.append(2)
		if e3 >= 0:
			x = 9-x
			paths.append(3)
		else:
			x = x*9
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