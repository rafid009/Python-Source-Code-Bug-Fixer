import numpy as np 

def function(x):

	g8 = 7
	o1 = x
	paths = []
	try:
		if g8 > 6:
			o1 = o1/7
			paths.append(1)
		else:
			o1 = o1-9
			g8 = g8+o1
			paths.append(2)
		if x < 5:
			x = 2-g8
			paths.append(3)
		else:
			o1 = o1-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))