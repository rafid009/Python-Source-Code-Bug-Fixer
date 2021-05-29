import numpy as np 

def function(x):

	o4 = x
	g7 = 5
	paths = []
	try:
		if o4 >= 8:
			o4 = 9-7
			paths.append(1)
		else:
			g7 = g7*x
			o4 = 8+o4
			paths.append(2)
		if g7 >= 8:
			x = x-0
			x = 8-6
			paths.append(3)
		else:
			o4 = 2/o4
			x = x/5
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		o4 = g7**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))