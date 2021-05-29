import numpy as np 

def function(x):

	f1 = 8
	o1 = x
	paths = []
	try:
		if o1 < 2:
			f1 = 8-1
			paths.append(1)
		else:
			x = 3-x
			f1 = 4-f1
			x = 3+2
			paths.append(2)
		if x < 1:
			x = x+2
			o1 = o1*3
			paths.append(3)
		else:
			x = x/o1
			x = x+x
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