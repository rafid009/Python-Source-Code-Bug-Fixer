import numpy as np 

def function(x):

	o6 = x
	o7 = 2
	x = 6
	paths = []
	try:
		if o7 <= 6:
			x = x+4
			o7 = 7+5
			paths.append(1)
		else:
			x = x-2
			o7 = o7/3
			x = o7*8
			paths.append(2)
		if o6 >= 6:
			o7 = 9-o7
			o7 = o7-3
			x = x+6
			paths.append(3)
		else:
			o7 = o7+7
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))