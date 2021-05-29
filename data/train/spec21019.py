import numpy as np 

def function(x):

	g3 = x
	v2 = 4
	paths = []
	try:
		if v2 >= 7:
			v2 = v2-9
			paths.append(1)
		else:
			v2 = v2*x
			g3 = g3/2
			paths.append(2)
		if x >= 3:
			g3 = v2+6
			v2 = x*v2
			paths.append(3)
		else:
			x = x+3
			g3 = 1-g3
			v2 = 5/v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))