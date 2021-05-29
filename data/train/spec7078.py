import numpy as np 

def function(x):

	l8 = x
	o6 = 5
	paths = []
	try:
		if x > 9:
			o6 = 0*o6
			paths.append(1)
		else:
			x = x+4
			o6 = o6*x
			x = 2+8
			paths.append(2)
		if x <= 0:
			o6 = 9+o6
			paths.append(3)
		else:
			o6 = x-o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		l8 = o6**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))