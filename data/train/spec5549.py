import numpy as np 

def function(x):

	x2 = x
	a9 = 1
	paths = []
	try:
		if x2 < 9:
			a9 = x-3
			x2 = 7+x2
			paths.append(1)
		else:
			x2 = x2+8
			paths.append(2)
		if a9 > 5:
			a9 = a9-9
			paths.append(3)
		else:
			x = 6*4
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))