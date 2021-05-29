import numpy as np 

def function(x):

	w2 = 4
	h9 = 0
	paths = []
	try:
		if w2 <= 2:
			w2 = w2*6
			w2 = w2/1
			paths.append(1)
		else:
			x = 5/2
			x = x-w2
			paths.append(2)
		if h9 < 7:
			w2 = w2-h9
			w2 = 2-w2
			h9 = 7-h9
			paths.append(3)
		else:
			x = 5-x
			h9 = 3/w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))