import numpy as np 

def function(x):

	w5 = 8
	e3 = x
	paths = []
	try:
		if x < 3:
			e3 = 8/x
			e3 = x/e3
			paths.append(1)
		else:
			w5 = 3-w5
			x = w5*x
			paths.append(2)
		if e3 < 9:
			w5 = e3/w5
			paths.append(3)
		else:
			w5 = 9+w5
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