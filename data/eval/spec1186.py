import numpy as np 

def function(x):

	w8 = x
	k2 = 4
	paths = []
	try:
		if x < 5:
			k2 = k2*4
			paths.append(1)
		else:
			w8 = k2*k2
			w8 = 1/7
			paths.append(2)
		if k2 < 7:
			w8 = w8*9
			x = x*x
			paths.append(3)
		else:
			w8 = 4+w8
			w8 = w8-8
			x = x+3
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