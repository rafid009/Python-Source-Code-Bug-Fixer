import numpy as np 

def function(x):

	b7 = 4
	w5 = 1
	paths = []
	try:
		if b7 >= 0:
			b7 = b7/b7
			b7 = 8-b7
			paths.append(1)
		else:
			b7 = b7/b7
			w5 = w5-w5
			x = 4*6
			paths.append(2)
		if w5 <= 4:
			x = b7-3
			x = x-b7
			paths.append(3)
		else:
			b7 = b7*2
			b7 = b7-b7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))