import numpy as np 

def function(x):

	r3 = 4
	g0 = x
	paths = []
	try:
		if g0 >= 2:
			r3 = 2-3
			paths.append(1)
		else:
			x = 2/x
			r3 = g0-6
			paths.append(2)
		if r3 > 3:
			x = x-1
			g0 = x+g0
			paths.append(3)
		else:
			x = 0+0
			g0 = 4+x
			g0 = g0*r3
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		r3 = g0**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))