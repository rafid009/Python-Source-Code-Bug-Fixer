import numpy as np 

def function(x):

	o6 = 7
	g7 = x
	paths = []
	try:
		if g7 < 3:
			g7 = x*g7
			g7 = 9-0
			o6 = x+o6
			paths.append(1)
		else:
			g7 = 3+g7
			o6 = o6/5
			g7 = 6+g7
			paths.append(2)
		if g7 < 5:
			x = x/g7
			o6 = o6*3
			paths.append(3)
		else:
			x = 3-x
			g7 = o6+g7
			o6 = o6*g7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))