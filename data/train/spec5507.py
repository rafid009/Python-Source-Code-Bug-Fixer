import numpy as np 

def function(x):

	r4 = x
	v2 = 6
	x = x
	paths = []
	try:
		if x > 6:
			r4 = r4*x
			x = x+v2
			r4 = 1+r4
			paths.append(1)
		else:
			r4 = x+r4
			paths.append(2)
		if x >= 3:
			v2 = v2-v2
			r4 = 1-r4
			paths.append(3)
		else:
			r4 = r4*r4
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))