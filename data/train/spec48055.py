import numpy as np 

def function(x):

	b8 = x
	w3 = x
	paths = []
	try:
		if x > 8:
			w3 = w3/6
			b8 = b8*7
			paths.append(1)
		else:
			b8 = b8*4
			paths.append(2)
		if x >= 8:
			w3 = 1-8
			paths.append(3)
		else:
			w3 = 2/w3
			w3 = w3-8
			w3 = 6*w3
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		w3 = b8**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))