import numpy as np 

def function(x):

	f2 = 0
	o6 = x
	paths = []
	try:
		if f2 < 5:
			f2 = 2-2
			paths.append(1)
		else:
			o6 = o6/9
			f2 = 5/f2
			f2 = 5*f2
			paths.append(2)
		if o6 <= 9:
			o6 = 2+o6
			x = 3-x
			paths.append(3)
		else:
			x = 3/x
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