import numpy as np 

def function(x):

	f0 = x
	o9 = 8
	paths = []
	try:
		if x < 3:
			o9 = o9+8
			x = 6/5
			f0 = 0-f0
			paths.append(1)
		else:
			f0 = x+8
			paths.append(2)
		if x < 3:
			f0 = f0+1
			o9 = x-9
			x = f0/x
			paths.append(3)
		else:
			o9 = o9/o9
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