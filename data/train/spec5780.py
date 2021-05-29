import numpy as np 

def function(x):

	a5 = 9
	w8 = x
	paths = []
	try:
		if x > 3:
			w8 = 9*w8
			paths.append(1)
		else:
			x = 5/x
			w8 = 1/3
			w8 = w8+x
			paths.append(2)
		if w8 < 6:
			w8 = w8/2
			a5 = x*x
			a5 = a5+8
			paths.append(3)
		else:
			w8 = x-1
			a5 = 6*a5
			w8 = w8+4
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))