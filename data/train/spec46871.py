import numpy as np 

def function(x):

	o2 = x
	x3 = 3
	paths = []
	try:
		if o2 < 6:
			o2 = o2/1
			paths.append(1)
		else:
			o2 = o2+3
			paths.append(2)
		if o2 >= 2:
			o2 = x3-5
			x3 = 5/x3
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))