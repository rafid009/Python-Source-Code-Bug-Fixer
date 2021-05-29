import numpy as np 

def function(x):

	r4 = x
	g0 = 6
	paths = []
	try:
		if x < 9:
			x = 5*r4
			paths.append(1)
		else:
			g0 = 9/4
			x = x+6
			paths.append(2)
		if g0 > 5:
			g0 = g0+g0
			paths.append(3)
		else:
			r4 = r4+5
			g0 = g0-9
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))