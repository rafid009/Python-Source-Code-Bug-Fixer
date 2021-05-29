import numpy as np 

def function(x):

	r3 = x
	e0 = 3
	paths = []
	try:
		if e0 >= 6:
			e0 = 3/e0
			paths.append(1)
		else:
			r3 = 5/r3
			paths.append(2)
		if r3 < 0:
			e0 = e0-4
			e0 = e0-4
			r3 = r3-1
			paths.append(3)
		else:
			x = 0+6
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))