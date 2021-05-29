import numpy as np 

def function(x):

	g0 = x
	v2 = x
	paths = []
	try:
		if g0 > 7:
			v2 = g0-7
			g0 = g0/2
			paths.append(1)
		else:
			v2 = v2-2
			paths.append(2)
		if g0 >= 3:
			g0 = g0-g0
			x = g0/4
			x = x+1
			paths.append(3)
		else:
			v2 = 6*g0
			v2 = 2/v2
			v2 = 2*g0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		v2 = g0**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))