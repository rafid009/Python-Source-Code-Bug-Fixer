import numpy as np 

def function(x):

	v0 = x
	o7 = 7
	paths = []
	try:
		if o7 >= 8:
			o7 = o7/o7
			x = o7-6
			paths.append(1)
		else:
			v0 = 0-v0
			x = x+x
			paths.append(2)
		if o7 > 8:
			o7 = 2+8
			x = 8*x
			v0 = v0-5
			paths.append(3)
		else:
			x = 6-4
			o7 = o7/v0
			o7 = 7/o7
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		v0 = o7**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))