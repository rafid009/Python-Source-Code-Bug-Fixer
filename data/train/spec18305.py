import numpy as np 

def function(x):

	w2 = 9
	s0 = 9
	x = x
	paths = []
	try:
		if x > 5:
			x = x+0
			w2 = w2-0
			paths.append(1)
		else:
			w2 = 0-w2
			paths.append(2)
		if w2 > 6:
			x = s0*3
			w2 = 7-w2
			paths.append(3)
		else:
			x = 9/x
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