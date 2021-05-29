import numpy as np 

def function(x):

	r6 = 9
	v3 = x
	paths = []
	try:
		if r6 > 0:
			x = x*6
			r6 = r6-6
			paths.append(1)
		else:
			r6 = x*r6
			r6 = 9/r6
			x = 4-r6
			paths.append(2)
		if r6 > 7:
			x = x-x
			v3 = 7/x
			x = v3-9
			paths.append(3)
		else:
			r6 = v3/3
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))