import numpy as np 

def function(x):

	g3 = x
	o8 = x
	x = 5
	paths = []
	try:
		if g3 < 4:
			g3 = g3+7
			x = g3/x
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if o8 < 2:
			g3 = o8*o8
			x = 2+x
			paths.append(3)
		else:
			o8 = o8+o8
			x = 6/x
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