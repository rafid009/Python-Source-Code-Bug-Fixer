import numpy as np 

def function(x):

	w2 = 4
	n8 = 6
	paths = []
	try:
		if w2 < 7:
			w2 = n8*w2
			x = w2*x
			w2 = 0*w2
			paths.append(1)
		else:
			w2 = 3/2
			paths.append(2)
		if x <= 1:
			w2 = w2+4
			paths.append(3)
		else:
			w2 = w2*3
			x = x/6
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