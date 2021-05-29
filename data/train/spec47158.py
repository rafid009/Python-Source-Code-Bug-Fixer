import numpy as np 

def function(x):

	a9 = 8
	o6 = x
	paths = []
	try:
		if o6 >= 6:
			o6 = 3*o6
			paths.append(1)
		else:
			x = x/1
			x = 9*o6
			a9 = a9+7
			paths.append(2)
		if o6 >= 6:
			x = 8-4
			a9 = a9+9
			a9 = 9-a9
			paths.append(3)
		else:
			a9 = 0*a9
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		a9 = o6**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))