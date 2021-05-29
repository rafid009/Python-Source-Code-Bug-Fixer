import numpy as np 

def function(x):

	w5 = x
	a5 = x
	paths = []
	try:
		if x >= 9:
			w5 = 1/w5
			paths.append(1)
		else:
			x = 9+x
			x = w5/x
			x = 1/x
			paths.append(2)
		if a5 < 0:
			a5 = a5/3
			paths.append(3)
		else:
			x = 9+w5
			w5 = 2+w5
			w5 = 3+w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))