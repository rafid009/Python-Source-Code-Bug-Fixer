import numpy as np 

def function(x):

	h2 = 1
	w7 = x
	paths = []
	try:
		if x > 4:
			w7 = 2+w7
			h2 = h2/3
			h2 = h2+7
			paths.append(1)
		else:
			w7 = 7-h2
			paths.append(2)
		if w7 < 7:
			w7 = 4*w7
			h2 = w7/6
			w7 = w7*3
			paths.append(3)
		else:
			w7 = h2/3
			w7 = 3*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))