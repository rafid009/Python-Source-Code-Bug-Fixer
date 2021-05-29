import numpy as np 

def function(x):

	g1 = x
	r3 = 7
	paths = []
	try:
		if g1 > 7:
			r3 = r3/8
			g1 = g1-0
			paths.append(1)
		else:
			r3 = 7-r3
			x = g1+7
			x = x+5
			paths.append(2)
		if g1 < 4:
			g1 = g1/5
			g1 = x/6
			g1 = r3-g1
			paths.append(3)
		else:
			x = 2/x
			x = 5-x
			r3 = r3+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))