import numpy as np 

def function(x):

	o2 = 9
	v3 = 3
	paths = []
	try:
		if o2 < 2:
			o2 = o2/8
			x = x*x
			paths.append(1)
		else:
			o2 = 1*6
			paths.append(2)
		if o2 < 2:
			o2 = 1/o2
			x = 4-o2
			paths.append(3)
		else:
			o2 = 0+4
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