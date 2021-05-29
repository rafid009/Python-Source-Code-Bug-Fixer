import numpy as np 

def function(x):

	o6 = x
	x8 = x
	paths = []
	try:
		if x8 < 7:
			o6 = o6+o6
			x = 3*x
			x = 8*o6
			paths.append(1)
		else:
			x = x8/9
			paths.append(2)
		if x > 6:
			x8 = 7-7
			paths.append(3)
		else:
			x = x+9
			o6 = 9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))