import numpy as np 

def function(x):

	e2 = 7
	r6 = x
	paths = []
	try:
		if r6 < 6:
			e2 = e2*x
			paths.append(1)
		else:
			e2 = r6/3
			e2 = e2+2
			paths.append(2)
		if x < 2:
			r6 = 2*9
			paths.append(3)
		else:
			r6 = x/3
			e2 = 6/6
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