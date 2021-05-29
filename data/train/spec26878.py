import numpy as np 

def function(x):

	a0 = x
	w7 = x
	paths = []
	try:
		if a0 > 8:
			x = x-2
			a0 = a0-6
			x = w7-2
			paths.append(1)
		else:
			x = x*x
			x = x+3
			paths.append(2)
		if w7 >= 9:
			w7 = w7-5
			paths.append(3)
		else:
			a0 = a0+2
			w7 = w7+0
			x = x-6
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