import numpy as np 

def function(x):

	w8 = 7
	a1 = x
	x = x
	paths = []
	try:
		if a1 >= 3:
			w8 = a1/w8
			w8 = 8-w8
			x = x+x
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x < 3:
			a1 = 0+x
			a1 = a1*w8
			paths.append(3)
		else:
			x = a1*w8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))