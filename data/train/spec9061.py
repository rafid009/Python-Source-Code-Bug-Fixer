import numpy as np 

def function(x):

	f0 = x
	n7 = x
	paths = []
	try:
		if f0 > 3:
			n7 = n7/4
			paths.append(1)
		else:
			f0 = f0*x
			paths.append(2)
		if n7 < 1:
			n7 = f0-9
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))