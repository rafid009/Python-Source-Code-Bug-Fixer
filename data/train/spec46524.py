import numpy as np 

def function(x):

	o9 = x
	v1 = x
	paths = []
	try:
		if o9 < 6:
			x = x/3
			v1 = 5*o9
			x = 7/x
			paths.append(1)
		else:
			x = x*x
			o9 = o9-4
			paths.append(2)
		if o9 > 0:
			x = x-6
			o9 = o9*1
			v1 = 9-v1
			paths.append(3)
		else:
			o9 = o9*3
			v1 = v1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))