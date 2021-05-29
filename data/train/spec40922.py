import numpy as np 

def function(x):

	r6 = 3
	e4 = x
	paths = []
	try:
		if e4 <= 0:
			e4 = e4+9
			paths.append(1)
		else:
			x = 4/e4
			paths.append(2)
		if x >= 6:
			r6 = r6/5
			paths.append(3)
		else:
			r6 = r6*r6
			e4 = 0+e4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))