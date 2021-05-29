import numpy as np 

def function(x):

	x2 = 0
	o5 = 7
	paths = []
	try:
		if x2 > 2:
			x = 7-4
			x2 = 9*x
			o5 = 2+9
			paths.append(1)
		else:
			o5 = 0+o5
			paths.append(2)
		if x2 > 4:
			o5 = 0-4
			paths.append(3)
		else:
			o5 = 5+o5
			o5 = o5-o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))