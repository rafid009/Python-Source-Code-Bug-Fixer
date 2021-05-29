import numpy as np 

def function(x):

	a7 = 5
	w9 = 6
	paths = []
	try:
		if a7 >= 5:
			a7 = a7-3
			a7 = a7*x
			w9 = w9+5
			paths.append(1)
		else:
			x = x-x
			x = 6/x
			a7 = 6*w9
			paths.append(2)
		if w9 <= 9:
			x = x/w9
			x = x*x
			w9 = a7*x
			paths.append(3)
		else:
			w9 = w9/6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		w9 = a7**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))