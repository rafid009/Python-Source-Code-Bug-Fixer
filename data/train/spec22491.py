import numpy as np 

def function(x):

	z1 = x
	w8 = 6
	x = 2
	paths = []
	try:
		if z1 < 1:
			x = 2/x
			w8 = w8/w8
			x = 9+0
			paths.append(1)
		else:
			x = x+5
			w8 = x-9
			x = x+x
			paths.append(2)
		if z1 >= 4:
			x = 6-x
			paths.append(3)
		else:
			w8 = w8-0
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))