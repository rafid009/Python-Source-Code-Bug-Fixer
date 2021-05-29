import numpy as np 

def function(x):

	r5 = x
	g4 = x
	paths = []
	try:
		if g4 < 6:
			g4 = g4-g4
			paths.append(1)
		else:
			x = 3-x
			x = 4-8
			x = 6/x
			paths.append(2)
		if x > 7:
			x = r5+1
			x = x*1
			g4 = r5/g4
			paths.append(3)
		else:
			r5 = 2*r5
			r5 = r5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))