import numpy as np 

def function(x):

	w2 = x
	y0 = x
	paths = []
	try:
		if w2 > 8:
			w2 = x/6
			w2 = x-w2
			paths.append(1)
		else:
			x = x-w2
			paths.append(2)
		if y0 < 8:
			w2 = 2*w2
			x = x-7
			paths.append(3)
		else:
			x = y0/4
			x = 8*2
			y0 = w2+y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))