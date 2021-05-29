import numpy as np 

def function(x):

	o7 = 9
	v8 = x
	paths = []
	try:
		if x >= 2:
			o7 = o7+0
			paths.append(1)
		else:
			x = 3/o7
			paths.append(2)
		if x > 2:
			x = x*v8
			o7 = 6-o7
			o7 = 0+o7
			paths.append(3)
		else:
			o7 = x-v8
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		v8 = o7**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))