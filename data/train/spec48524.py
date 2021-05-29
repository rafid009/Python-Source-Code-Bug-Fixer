import numpy as np 

def function(x):

	v6 = 8
	g0 = 7
	paths = []
	try:
		if x >= 0:
			v6 = v6*4
			g0 = g0+2
			x = 6-x
			paths.append(1)
		else:
			v6 = g0/1
			paths.append(2)
		if v6 > 2:
			v6 = x*v6
			paths.append(3)
		else:
			x = v6/x
			v6 = g0+v6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))