import numpy as np 

def function(x):

	r6 = x
	g3 = 9
	paths = []
	try:
		if r6 < 1:
			x = x+9
			x = x+g3
			paths.append(1)
		else:
			r6 = g3*6
			r6 = 5/r6
			g3 = g3/2
			paths.append(2)
		if x > 2:
			r6 = 8*r6
			r6 = x+0
			paths.append(3)
		else:
			g3 = g3/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))