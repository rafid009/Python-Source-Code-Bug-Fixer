import numpy as np 

def function(x):

	w1 = 4
	g1 = x
	paths = []
	try:
		if g1 < 9:
			w1 = w1-8
			paths.append(1)
		else:
			w1 = 9-w1
			x = x+x
			paths.append(2)
		if g1 > 9:
			w1 = g1/x
			g1 = 1+g1
			paths.append(3)
		else:
			x = x+g1
			g1 = g1*9
			w1 = 6/w1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))