import numpy as np 

def function(x):

	o6 = x
	o5 = x
	paths = []
	try:
		if o5 < 2:
			o5 = o5+7
			paths.append(1)
		else:
			o5 = 2*o5
			o6 = o6+6
			paths.append(2)
		if o5 >= 9:
			o5 = o5+4
			paths.append(3)
		else:
			o5 = 8-o5
			o6 = 8+o6
			o5 = 9+o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))