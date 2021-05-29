import numpy as np 

def function(x):

	w8 = 7
	f1 = x
	paths = []
	try:
		if w8 >= 0:
			w8 = w8/f1
			w8 = 7+w8
			paths.append(1)
		else:
			w8 = 6/w8
			paths.append(2)
		if x >= 0:
			f1 = f1/8
			paths.append(3)
		else:
			w8 = 2*2
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