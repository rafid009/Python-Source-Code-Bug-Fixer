import numpy as np 

def function(x):

	g5 = x
	r6 = x
	paths = []
	try:
		if r6 < 4:
			g5 = g5-9
			paths.append(1)
		else:
			x = x+4
			g5 = 6*g5
			g5 = g5-3
			paths.append(2)
		if g5 > 5:
			x = x+x
			paths.append(3)
		else:
			r6 = r6/r6
			r6 = r6+r6
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