import numpy as np 

def function(x):

	n2 = 8
	f0 = 1
	paths = []
	try:
		if n2 <= 2:
			n2 = 1/f0
			n2 = 1/n2
			paths.append(1)
		else:
			n2 = 5*3
			f0 = 2*f0
			paths.append(2)
		if x <= 7:
			x = x-f0
			n2 = 8-n2
			f0 = 8/2
			paths.append(3)
		else:
			x = f0/x
			x = 5+4
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