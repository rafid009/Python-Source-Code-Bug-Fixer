import numpy as np 

def function(x):

	r4 = 8
	v7 = x
	paths = []
	try:
		if v7 <= 3:
			r4 = 4+r4
			x = x*3
			paths.append(1)
		else:
			v7 = 2+v7
			r4 = x*6
			paths.append(2)
		if v7 < 3:
			r4 = 8/r4
			paths.append(3)
		else:
			r4 = 9/r4
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