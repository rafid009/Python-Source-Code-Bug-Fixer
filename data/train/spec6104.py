import numpy as np 

def function(x):

	v3 = x
	o8 = 9
	paths = []
	try:
		if o8 >= 5:
			x = 4-2
			paths.append(1)
		else:
			v3 = 1*v3
			x = 3-x
			paths.append(2)
		if x > 7:
			o8 = 5/v3
			x = x+7
			x = x+4
			paths.append(3)
		else:
			x = x-3
			o8 = o8-4
			v3 = v3-4
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