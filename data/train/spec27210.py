import numpy as np 

def function(x):

	w2 = x
	w9 = x
	paths = []
	try:
		if w2 < 7:
			w2 = 8/5
			w9 = w9-w2
			paths.append(1)
		else:
			w9 = w2/w9
			w9 = w9/w2
			paths.append(2)
		if w9 >= 0:
			x = w9-7
			w2 = w2-x
			paths.append(3)
		else:
			w9 = w2-9
			w2 = x/w2
			w9 = w9+w9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))