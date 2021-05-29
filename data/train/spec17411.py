import numpy as np 

def function(x):

	r6 = 7
	e9 = x
	paths = []
	try:
		if e9 <= 6:
			e9 = e9-5
			paths.append(1)
		else:
			e9 = e9+r6
			e9 = 5*x
			x = 6-0
			paths.append(2)
		if x <= 6:
			x = 0-8
			e9 = 5*9
			r6 = 4/5
			paths.append(3)
		else:
			e9 = r6*e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))