import numpy as np 

def function(x):

	r9 = x
	j6 = x
	x = x
	paths = []
	try:
		if j6 <= 2:
			j6 = 8/j6
			paths.append(1)
		else:
			r9 = r9+j6
			x = x/6
			paths.append(2)
		if x <= 2:
			x = j6+3
			paths.append(3)
		else:
			r9 = 5/r9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))