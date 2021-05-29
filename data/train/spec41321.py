import numpy as np 

def function(x):

	g4 = x
	o0 = x
	paths = []
	try:
		if o0 < 1:
			o0 = o0+o0
			o0 = 6/x
			paths.append(1)
		else:
			g4 = 9/g4
			paths.append(2)
		if g4 < 2:
			o0 = 0-o0
			x = 6*g4
			o0 = 5+2
			paths.append(3)
		else:
			o0 = x*x
			o0 = 3-o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))