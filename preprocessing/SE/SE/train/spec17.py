import numpy as np 

def function(x):

	o1 = x
	v4 = x
	paths = []
	try:
		if x > 5:
			v4 = 1+8
			x = 1/x
			x = x+5
			paths.append(1)
		else:
			x = o1-x
			o1 = x-4
			x = 8*o1
			paths.append(2)
		if v4 > 1:
			x = v4/x
			paths.append(3)
		else:
			v4 = v4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))