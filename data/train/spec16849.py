import numpy as np 

def function(x):

	r9 = x
	v7 = 2
	paths = []
	try:
		if r9 < 2:
			r9 = 1/r9
			r9 = r9*0
			paths.append(1)
		else:
			v7 = v7/x
			paths.append(2)
		if r9 <= 3:
			v7 = x/v7
			r9 = 3-9
			paths.append(3)
		else:
			x = v7+4
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))