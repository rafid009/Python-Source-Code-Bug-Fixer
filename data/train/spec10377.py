import numpy as np 

def function(x):

	g0 = 5
	o2 = 4
	paths = []
	try:
		if x > 9:
			o2 = g0*o2
			paths.append(1)
		else:
			x = x+0
			o2 = o2+9
			paths.append(2)
		if x >= 0:
			x = x-5
			paths.append(3)
		else:
			g0 = 4+g0
			o2 = 1-o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		g0 = o2**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))