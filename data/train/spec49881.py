import numpy as np 

def function(x):

	o4 = 5
	g1 = x
	paths = []
	try:
		if o4 > 6:
			g1 = 8*g1
			g1 = 7*g1
			paths.append(1)
		else:
			o4 = o4*9
			paths.append(2)
		if x <= 5:
			g1 = g1/1
			x = 2-2
			o4 = 4/1
			paths.append(3)
		else:
			o4 = g1+o4
			g1 = 9/g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))