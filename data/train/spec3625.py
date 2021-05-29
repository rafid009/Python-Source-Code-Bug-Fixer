import numpy as np 

def function(x):

	g0 = x
	d7 = x
	paths = []
	try:
		if g0 > 0:
			g0 = g0*3
			x = x/2
			paths.append(1)
		else:
			d7 = 4/1
			paths.append(2)
		if g0 > 9:
			x = g0*0
			paths.append(3)
		else:
			x = x/9
			x = 2*g0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))