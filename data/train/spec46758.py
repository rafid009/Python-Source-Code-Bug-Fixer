import numpy as np 

def function(x):

	j0 = 0
	o1 = 1
	paths = []
	try:
		if o1 > 0:
			o1 = 4*8
			j0 = 4+8
			paths.append(1)
		else:
			o1 = o1/9
			paths.append(2)
		if x <= 1:
			o1 = 8/5
			paths.append(3)
		else:
			j0 = j0-6
			j0 = o1/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))