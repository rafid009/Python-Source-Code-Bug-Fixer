import numpy as np 

def function(x):

	j7 = 6
	r2 = x
	paths = []
	try:
		if j7 <= 2:
			r2 = r2-3
			j7 = 4*j7
			x = 5/x
			paths.append(1)
		else:
			j7 = j7/r2
			j7 = 5+j7
			paths.append(2)
		if j7 <= 6:
			x = 2/x
			r2 = 1/x
			x = 6-9
			paths.append(3)
		else:
			x = 9-1
			r2 = 0-j7
			j7 = 4/r2
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