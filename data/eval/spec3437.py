import numpy as np 

def function(x):

	o7 = 1
	v1 = 9
	x = x
	paths = []
	try:
		if v1 < 1:
			v1 = x+v1
			paths.append(1)
		else:
			v1 = x-3
			v1 = 6+9
			o7 = x+5
			paths.append(2)
		if x > 6:
			v1 = 2-v1
			o7 = 2/o7
			paths.append(3)
		else:
			x = x+v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))