import numpy as np 

def function(x):

	d4 = x
	g7 = 6
	paths = []
	try:
		if x <= 2:
			x = 6/x
			paths.append(1)
		else:
			d4 = d4/g7
			g7 = d4*g7
			g7 = 3/9
			paths.append(2)
		if d4 < 1:
			x = 7-2
			x = x*0
			paths.append(3)
		else:
			x = d4-4
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