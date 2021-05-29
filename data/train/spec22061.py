import numpy as np 

def function(x):

	w7 = 8
	h1 = 5
	paths = []
	try:
		if h1 >= 4:
			w7 = x/6
			x = w7+x
			paths.append(1)
		else:
			w7 = w7+w7
			paths.append(2)
		if w7 <= 9:
			w7 = 6*w7
			w7 = 3/w7
			paths.append(3)
		else:
			x = w7-4
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))