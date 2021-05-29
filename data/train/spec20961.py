import numpy as np 

def function(x):

	w2 = x
	x0 = 1
	paths = []
	try:
		if x0 >= 6:
			x = x+5
			x = w2-5
			paths.append(1)
		else:
			x0 = x0+1
			paths.append(2)
		if x >= 5:
			w2 = 0*w2
			w2 = 8-w2
			paths.append(3)
		else:
			x0 = 1+x0
			x = x/x0
			x = x-1
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