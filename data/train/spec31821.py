import numpy as np 

def function(x):

	e3 = 4
	v2 = x
	paths = []
	try:
		if v2 < 7:
			e3 = e3/x
			v2 = v2-v2
			e3 = e3*9
			paths.append(1)
		else:
			x = e3*5
			paths.append(2)
		if v2 >= 9:
			e3 = e3*6
			v2 = 9+v2
			x = x/x
			paths.append(3)
		else:
			e3 = e3*9
			x = 2-x
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