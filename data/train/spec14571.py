import numpy as np 

def function(x):

	g1 = x
	r1 = 4
	paths = []
	try:
		if g1 <= 7:
			r1 = r1*x
			x = x-r1
			r1 = 8/r1
			paths.append(1)
		else:
			x = x+5
			x = 4-x
			paths.append(2)
		if x > 9:
			g1 = g1*1
			paths.append(3)
		else:
			r1 = r1+x
			g1 = x+4
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