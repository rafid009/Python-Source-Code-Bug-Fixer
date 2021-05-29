import numpy as np 

def function(x):

	w2 = 1
	w8 = x
	paths = []
	try:
		if w8 > 9:
			w8 = w8-1
			paths.append(1)
		else:
			w2 = 0-w2
			w8 = w2*5
			paths.append(2)
		if w2 > 2:
			x = 1/x
			paths.append(3)
		else:
			w8 = w8*2
			w2 = w2-9
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))