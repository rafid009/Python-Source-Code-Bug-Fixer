import numpy as np 

def function(x):

	x3 = x
	r6 = x
	paths = []
	try:
		if x >= 3:
			r6 = r6/9
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x3 > 5:
			x = 8/x
			paths.append(3)
		else:
			r6 = x3/r6
			x = x3/7
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