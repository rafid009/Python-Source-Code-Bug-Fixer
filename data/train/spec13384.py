import numpy as np 

def function(x):

	o5 = 0
	l6 = 8
	paths = []
	try:
		if o5 < 6:
			o5 = l6-2
			paths.append(1)
		else:
			l6 = l6*6
			paths.append(2)
		if o5 >= 9:
			x = x-0
			o5 = o5*o5
			paths.append(3)
		else:
			l6 = l6/2
			l6 = l6/5
			o5 = o5-4
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