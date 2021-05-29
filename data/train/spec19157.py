import numpy as np 

def function(x):

	v1 = 9
	o0 = x
	paths = []
	try:
		if x >= 0:
			x = 2+x
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if v1 >= 5:
			o0 = 3-o0
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		v1 = o0**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))