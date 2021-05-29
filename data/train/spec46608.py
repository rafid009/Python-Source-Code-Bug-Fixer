import numpy as np 

def function(x):

	o6 = x
	o4 = 4
	paths = []
	try:
		if x >= 0:
			o6 = o6+4
			paths.append(1)
		else:
			o6 = o4-o6
			o6 = 9/x
			o4 = o6*7
			paths.append(2)
		if o4 > 1:
			x = o4-6
			paths.append(3)
		else:
			x = 5/x
			x = x/x
			o6 = o6-1
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))