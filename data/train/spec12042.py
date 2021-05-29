import numpy as np 

def function(x):

	w8 = 8
	b7 = 5
	paths = []
	try:
		if w8 <= 3:
			w8 = 4*w8
			x = x+0
			paths.append(1)
		else:
			w8 = 0+0
			x = x/3
			paths.append(2)
		if w8 > 2:
			w8 = w8+b7
			x = 2*x
			paths.append(3)
		else:
			w8 = 2*w8
			x = x+9
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