import numpy as np 

def function(x):

	r4 = x
	e9 = 7
	paths = []
	try:
		if r4 < 6:
			x = 4-x
			paths.append(1)
		else:
			x = x*e9
			e9 = 9-e9
			paths.append(2)
		if r4 >= 6:
			e9 = 5-e9
			e9 = e9-5
			paths.append(3)
		else:
			r4 = r4+r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))