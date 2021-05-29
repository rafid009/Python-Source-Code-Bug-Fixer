import numpy as np 

def function(x):

	x4 = 9
	o9 = 6
	paths = []
	try:
		if x4 <= 5:
			o9 = 0*2
			paths.append(1)
		else:
			o9 = o9+3
			x4 = x4+5
			paths.append(2)
		if x >= 5:
			x4 = x4/1
			x = 1*x4
			x4 = x4-3
			paths.append(3)
		else:
			x4 = 9*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))