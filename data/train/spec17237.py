import numpy as np 

def function(x):

	g0 = x
	j2 = 8
	x = 1
	paths = []
	try:
		if g0 <= 2:
			g0 = g0*6
			paths.append(1)
		else:
			x = 6/x
			j2 = 9*j2
			x = 4/x
			paths.append(2)
		if g0 > 3:
			x = x*g0
			x = 6*7
			paths.append(3)
		else:
			j2 = 1+j2
			g0 = g0-5
			g0 = g0*8
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