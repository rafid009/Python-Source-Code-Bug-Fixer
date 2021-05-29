import numpy as np 

def function(x):

	w7 = 8
	w2 = 5
	paths = []
	try:
		if x >= 1:
			x = x-w2
			paths.append(1)
		else:
			x = w7/x
			w7 = w7+4
			x = x*2
			paths.append(2)
		if x >= 4:
			x = x+7
			x = 5/x
			w7 = w7+9
			paths.append(3)
		else:
			w7 = 4+w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))