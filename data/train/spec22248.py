import numpy as np 

def function(x):

	o0 = x
	g4 = 3
	paths = []
	try:
		if g4 < 8:
			x = x+g4
			o0 = o0+g4
			x = 2-g4
			paths.append(1)
		else:
			o0 = o0-x
			paths.append(2)
		if x >= 8:
			x = o0/x
			g4 = g4+g4
			x = x/5
			paths.append(3)
		else:
			o0 = x+o0
			x = x*2
			o0 = o0*o0
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