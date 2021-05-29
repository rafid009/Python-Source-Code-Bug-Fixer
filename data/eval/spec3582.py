import numpy as np 

def function(x):

	f1 = x
	n5 = x
	paths = []
	try:
		if n5 < 4:
			n5 = 9-5
			paths.append(1)
		else:
			x = 6+n5
			paths.append(2)
		if f1 > 5:
			f1 = 3*f1
			f1 = 4*f1
			paths.append(3)
		else:
			f1 = x-f1
			f1 = 1/6
			f1 = f1-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))