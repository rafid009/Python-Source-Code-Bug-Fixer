import numpy as np 

def function(x):

	x0 = 1
	w5 = x
	paths = []
	try:
		if w5 >= 5:
			x = x0*8
			paths.append(1)
		else:
			x0 = 4/w5
			paths.append(2)
		if x0 < 1:
			x0 = 2/x0
			paths.append(3)
		else:
			x0 = x0/3
			x0 = 2*x
			w5 = w5+8
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x0 = w5**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))