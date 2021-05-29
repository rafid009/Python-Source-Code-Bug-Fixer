import numpy as np 

def function(x):

	e4 = x
	r2 = 1
	x = 3
	paths = []
	try:
		if x >= 3:
			e4 = e4-r2
			x = r2*6
			r2 = r2*e4
			paths.append(1)
		else:
			e4 = e4*6
			r2 = 4*6
			e4 = x*e4
			paths.append(2)
		if r2 <= 3:
			e4 = e4-6
			r2 = 8/r2
			x = r2/e4
			paths.append(3)
		else:
			r2 = r2-r2
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))