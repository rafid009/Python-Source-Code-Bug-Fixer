import numpy as np 

def function(x):

	r2 = x
	j6 = 9
	paths = []
	try:
		if r2 < 3:
			r2 = x-7
			paths.append(1)
		else:
			r2 = 4/r2
			paths.append(2)
		if r2 < 7:
			x = r2/x
			paths.append(3)
		else:
			x = j6-6
			x = r2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))