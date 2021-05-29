import numpy as np 

def function(x):

	w1 = x
	k2 = 0
	paths = []
	try:
		if w1 > 9:
			x = 1/x
			w1 = w1+5
			k2 = 7*k2
			paths.append(1)
		else:
			k2 = 5+3
			paths.append(2)
		if x >= 6:
			w1 = w1/w1
			w1 = w1+w1
			w1 = k2/x
			paths.append(3)
		else:
			w1 = 1/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))