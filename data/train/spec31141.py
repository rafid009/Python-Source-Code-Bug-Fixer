import numpy as np 

def function(x):

	w8 = 3
	b1 = x
	x = x
	paths = []
	try:
		if b1 > 6:
			w8 = w8*w8
			b1 = b1/1
			w8 = b1*w8
			paths.append(1)
		else:
			b1 = x-b1
			b1 = b1*x
			paths.append(2)
		if w8 >= 3:
			b1 = x*7
			x = b1-x
			w8 = w8*2
			paths.append(3)
		else:
			w8 = w8-5
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