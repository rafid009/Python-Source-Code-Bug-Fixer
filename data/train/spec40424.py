import numpy as np 

def function(x):

	g2 = x
	o4 = x
	paths = []
	try:
		if x <= 2:
			x = 3-9
			o4 = 9/o4
			o4 = 8/o4
			paths.append(1)
		else:
			o4 = o4*o4
			o4 = 5/o4
			paths.append(2)
		if x > 4:
			o4 = x+4
			paths.append(3)
		else:
			g2 = 5+2
			x = x*5
			x = 1/x
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