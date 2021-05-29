import numpy as np 

def function(x):

	n5 = x
	f6 = 7
	paths = []
	try:
		if x > 9:
			n5 = n5/8
			paths.append(1)
		else:
			n5 = x-3
			paths.append(2)
		if x > 6:
			f6 = 6*f6
			paths.append(3)
		else:
			x = x+1
			f6 = f6*f6
			f6 = f6+5
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