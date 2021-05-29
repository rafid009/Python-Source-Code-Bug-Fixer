import numpy as np 

def function(x):

	b4 = 2
	w5 = x
	paths = []
	try:
		if x >= 1:
			w5 = w5-2
			paths.append(1)
		else:
			b4 = b4-9
			b4 = 3*b4
			paths.append(2)
		if w5 >= 1:
			x = 1*x
			w5 = b4-9
			paths.append(3)
		else:
			w5 = w5-w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		b4 = w5**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))