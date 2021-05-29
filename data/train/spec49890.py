import numpy as np 

def function(x):

	o1 = 5
	x4 = 5
	paths = []
	try:
		if o1 > 6:
			o1 = o1/o1
			paths.append(1)
		else:
			o1 = o1*4
			x4 = 2-x4
			paths.append(2)
		if o1 >= 4:
			x = o1*x
			x4 = 6-x
			paths.append(3)
		else:
			x = x+4
			x = o1*x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))