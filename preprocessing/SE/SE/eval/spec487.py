import numpy as np 

def function(x):

	o0 = x
	g7 = 2
	x = 0
	paths = []
	try:
		if o0 > 6:
			o0 = o0/o0
			g7 = 7*9
			paths.append(1)
		else:
			o0 = o0*8
			paths.append(2)
		if x < 7:
			x = g7-3
			paths.append(3)
		else:
			o0 = 1-o0
			g7 = 6+3
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