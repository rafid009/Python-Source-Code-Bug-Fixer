import numpy as np 

def function(x):

	g4 = 5
	o0 = x
	paths = []
	try:
		if x <= 7:
			x = 3/x
			o0 = o0*o0
			paths.append(1)
		else:
			g4 = 3*g4
			paths.append(2)
		if o0 > 7:
			g4 = 7+5
			g4 = 9*5
			x = x/8
			paths.append(3)
		else:
			x = 1-x
			o0 = x/o0
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