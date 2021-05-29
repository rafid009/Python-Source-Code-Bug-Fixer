import numpy as np 

def function(x):

	x8 = 2
	w8 = x
	paths = []
	try:
		if x < 0:
			x8 = x8-8
			paths.append(1)
		else:
			x8 = 0+x8
			x8 = x8/x
			paths.append(2)
		if x8 <= 8:
			x8 = x8/2
			x = 2-x
			w8 = 9*x8
			paths.append(3)
		else:
			x8 = 3*x8
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