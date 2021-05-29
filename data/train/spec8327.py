import numpy as np 

def function(x):

	v4 = 1
	o6 = 1
	x = x
	paths = []
	try:
		if o6 >= 5:
			x = 7-x
			paths.append(1)
		else:
			o6 = 9*o6
			paths.append(2)
		if o6 >= 1:
			o6 = 7*o6
			paths.append(3)
		else:
			v4 = v4+3
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