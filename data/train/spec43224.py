import numpy as np 

def function(x):

	v3 = 7
	r4 = x
	x = x
	paths = []
	try:
		if r4 <= 8:
			r4 = v3-9
			r4 = r4*x
			x = 4-6
			paths.append(1)
		else:
			v3 = v3*v3
			paths.append(2)
		if v3 <= 1:
			v3 = r4-r4
			r4 = 9-0
			paths.append(3)
		else:
			r4 = r4+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))