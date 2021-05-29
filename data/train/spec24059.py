import numpy as np 

def function(x):

	o8 = 3
	v6 = 7
	paths = []
	try:
		if o8 < 1:
			v6 = x-3
			x = v6-1
			v6 = v6/2
			paths.append(1)
		else:
			o8 = 3+5
			v6 = 0-v6
			paths.append(2)
		if o8 > 3:
			o8 = 1/o8
			v6 = x/3
			o8 = 5*o8
			paths.append(3)
		else:
			o8 = x/o8
			o8 = 6/3
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