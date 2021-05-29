import numpy as np 

def function(x):

	n7 = 8
	f7 = x
	paths = []
	try:
		if f7 < 1:
			n7 = f7*7
			n7 = 7+n7
			paths.append(1)
		else:
			x = 2+4
			n7 = n7/x
			n7 = n7*4
			paths.append(2)
		if n7 < 7:
			n7 = 5*f7
			paths.append(3)
		else:
			f7 = f7-f7
			f7 = 6-x
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