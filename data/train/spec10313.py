import numpy as np 

def function(x):

	o0 = x
	x4 = 4
	paths = []
	try:
		if x4 < 0:
			x4 = x4/7
			o0 = 2+x
			paths.append(1)
		else:
			x4 = 3*x4
			x4 = x4+4
			o0 = o0+3
			paths.append(2)
		if x4 <= 7:
			o0 = 6*o0
			paths.append(3)
		else:
			o0 = o0+o0
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