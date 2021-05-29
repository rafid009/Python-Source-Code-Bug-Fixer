import numpy as np 

def function(x):

	g2 = x
	o0 = 2
	x = 4
	paths = []
	try:
		if o0 < 6:
			g2 = o0-7
			o0 = o0+6
			paths.append(1)
		else:
			x = 7*9
			x = 4-g2
			paths.append(2)
		if o0 >= 0:
			o0 = x+o0
			x = 6/x
			o0 = 9*o0
			paths.append(3)
		else:
			x = 8/o0
			x = x*3
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))