import numpy as np 

def function(x):

	o5 = 5
	u6 = 9
	paths = []
	try:
		if x < 6:
			o5 = 7*o5
			u6 = o5/3
			paths.append(1)
		else:
			x = 8+x
			o5 = 1/o5
			paths.append(2)
		if o5 < 6:
			o5 = o5+x
			paths.append(3)
		else:
			u6 = 7-x
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