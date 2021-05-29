import numpy as np 

def function(x):

	w5 = 5
	b8 = x
	paths = []
	try:
		if x > 4:
			b8 = 6/w5
			paths.append(1)
		else:
			w5 = w5*7
			x = b8+4
			paths.append(2)
		if b8 > 7:
			b8 = 5*4
			w5 = x/x
			paths.append(3)
		else:
			w5 = 3/w5
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