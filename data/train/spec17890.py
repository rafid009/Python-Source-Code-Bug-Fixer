import numpy as np 

def function(x):

	d8 = x
	g3 = 4
	x = x
	paths = []
	try:
		if x < 1:
			g3 = g3*9
			g3 = d8/x
			paths.append(1)
		else:
			x = 9-3
			paths.append(2)
		if g3 < 6:
			d8 = g3-9
			g3 = d8/5
			paths.append(3)
		else:
			g3 = g3/d8
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		d8 = g3**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))