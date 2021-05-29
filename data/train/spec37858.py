import numpy as np 

def function(x):

	o6 = 3
	paths = []
	try:
		if o6 > 7:
			o6 = 6*o6
			o6 = o6+o6
			paths.append(1)
		else:
			o6 = o6/9
			o6 = o6*o6
			paths.append(2)
		if o6 >= 0:
			o6 = o6/8
			paths.append(3)
		else:
			o6 = o6-8
			o6 = o6/2
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