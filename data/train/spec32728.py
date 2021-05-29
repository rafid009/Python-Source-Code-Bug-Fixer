import numpy as np 

def function(x):

	b4 = x
	w8 = 8
	paths = []
	try:
		if w8 >= 4:
			x = x*5
			b4 = 4/b4
			paths.append(1)
		else:
			w8 = w8-6
			w8 = b4/w8
			paths.append(2)
		if w8 >= 6:
			w8 = w8-x
			b4 = 2-b4
			paths.append(3)
		else:
			b4 = b4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))