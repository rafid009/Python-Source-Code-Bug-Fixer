import numpy as np 

def function(x):

	o8 = 4
	g4 = 4
	paths = []
	try:
		if o8 > 5:
			o8 = 2+o8
			paths.append(1)
		else:
			o8 = o8/o8
			o8 = o8/6
			o8 = 5-o8
			paths.append(2)
		if g4 <= 2:
			o8 = o8+3
			x = x-x
			paths.append(3)
		else:
			o8 = o8/x
			g4 = 2-g4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))