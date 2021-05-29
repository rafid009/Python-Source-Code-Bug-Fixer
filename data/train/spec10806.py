import numpy as np 

def function(x):

	g2 = 0
	r3 = x
	paths = []
	try:
		if x <= 0:
			r3 = 6-0
			paths.append(1)
		else:
			r3 = x/r3
			x = x/8
			paths.append(2)
		if g2 > 0:
			r3 = 9-r3
			paths.append(3)
		else:
			g2 = g2-g2
			r3 = 4+4
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