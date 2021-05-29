import numpy as np 

def function(x):

	g1 = x
	r5 = 1
	paths = []
	try:
		if x <= 6:
			r5 = 6+x
			r5 = 1/r5
			g1 = 3-4
			paths.append(1)
		else:
			g1 = g1/5
			r5 = 2+r5
			paths.append(2)
		if x > 1:
			x = x*9
			r5 = 2*r5
			g1 = g1*8
			paths.append(3)
		else:
			g1 = g1-g1
			r5 = r5+6
			r5 = 4/r5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))