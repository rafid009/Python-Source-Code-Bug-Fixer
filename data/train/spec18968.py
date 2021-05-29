import numpy as np 

def function(x):

	w2 = 2
	g1 = x
	paths = []
	try:
		if w2 < 8:
			w2 = 6/g1
			paths.append(1)
		else:
			x = 6+8
			paths.append(2)
		if x <= 0:
			g1 = g1-9
			paths.append(3)
		else:
			g1 = g1/8
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))