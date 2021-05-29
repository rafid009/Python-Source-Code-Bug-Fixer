import numpy as np 

def function(x):

	w6 = 9
	g6 = x
	paths = []
	try:
		if x <= 2:
			x = x+4
			w6 = w6-3
			x = x*w6
			paths.append(1)
		else:
			w6 = w6/9
			paths.append(2)
		if g6 >= 3:
			g6 = 5*4
			x = x+x
			paths.append(3)
		else:
			x = 1/8
			x = x-9
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