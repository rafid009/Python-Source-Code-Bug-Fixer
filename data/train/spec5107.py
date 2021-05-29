import numpy as np 

def function(x):

	o7 = 1
	v4 = x
	paths = []
	try:
		if o7 > 4:
			x = 5/x
			x = o7-x
			o7 = o7+v4
			paths.append(1)
		else:
			o7 = o7/4
			v4 = v4-2
			paths.append(2)
		if x > 0:
			v4 = 3+v4
			v4 = v4*4
			paths.append(3)
		else:
			v4 = 6-v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))