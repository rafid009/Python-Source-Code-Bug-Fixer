import numpy as np 

def function(x):

	e2 = x
	r2 = 8
	paths = []
	try:
		if r2 < 8:
			e2 = 7-e2
			paths.append(1)
		else:
			x = x-8
			e2 = e2+6
			x = 5+x
			paths.append(2)
		if e2 >= 3:
			r2 = 2*r2
			paths.append(3)
		else:
			r2 = 4*r2
			r2 = 5/x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))