import numpy as np 

def function(x):

	j8 = 2
	w7 = x
	x = 1
	paths = []
	try:
		if j8 < 6:
			x = 4*5
			x = x*w7
			paths.append(1)
		else:
			x = x/j8
			w7 = w7+5
			paths.append(2)
		if w7 < 1:
			w7 = 8/6
			w7 = 7+0
			paths.append(3)
		else:
			w7 = w7*j8
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