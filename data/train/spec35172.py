import numpy as np 

def function(x):

	g4 = x
	r8 = x
	paths = []
	try:
		if r8 > 2:
			r8 = 1/4
			paths.append(1)
		else:
			r8 = r8/g4
			paths.append(2)
		if x > 2:
			g4 = g4-r8
			g4 = r8-g4
			x = r8/5
			paths.append(3)
		else:
			g4 = g4*x
			r8 = r8*x
			x = r8-5
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		r8 = g4**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))