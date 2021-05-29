import numpy as np 

def function(x):

	a5 = 2
	o6 = 0
	paths = []
	try:
		if a5 >= 8:
			x = x-3
			o6 = 1*o6
			paths.append(1)
		else:
			o6 = 8+6
			paths.append(2)
		if a5 > 5:
			a5 = 3*a5
			a5 = a5*2
			o6 = o6+o6
			paths.append(3)
		else:
			o6 = a5/9
			o6 = o6+7
			a5 = 9+a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))