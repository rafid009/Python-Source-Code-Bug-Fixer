import numpy as np 

def function(x):

	n3 = x
	o2 = 7
	x = x
	paths = []
	try:
		if o2 < 0:
			x = 1*x
			n3 = n3-x
			paths.append(1)
		else:
			o2 = 0*5
			paths.append(2)
		if n3 <= 7:
			n3 = n3+n3
			x = x/3
			paths.append(3)
		else:
			x = 7-2
			n3 = x-0
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