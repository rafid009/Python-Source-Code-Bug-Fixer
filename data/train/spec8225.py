import numpy as np 

def function(x):

	g4 = x
	r0 = x
	paths = []
	try:
		if g4 < 5:
			r0 = 3/r0
			x = x*r0
			paths.append(1)
		else:
			r0 = r0*3
			paths.append(2)
		if g4 >= 6:
			x = x/3
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))