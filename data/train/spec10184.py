import numpy as np 

def function(x):

	o5 = x
	q7 = x
	x = x
	paths = []
	try:
		if q7 > 0:
			o5 = 0/4
			paths.append(1)
		else:
			q7 = x+9
			paths.append(2)
		if o5 < 1:
			o5 = x+3
			o5 = 0+o5
			paths.append(3)
		else:
			x = o5+x
			o5 = 8+o5
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