import numpy as np 

def function(x):

	g3 = 6
	t0 = x
	x = x
	paths = []
	try:
		if g3 <= 8:
			g3 = 3+g3
			x = x/5
			paths.append(1)
		else:
			x = 8/x
			x = 0+g3
			paths.append(2)
		if g3 <= 1:
			g3 = g3-7
			t0 = t0*1
			x = 5-4
			paths.append(3)
		else:
			g3 = g3/4
			g3 = t0-g3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))