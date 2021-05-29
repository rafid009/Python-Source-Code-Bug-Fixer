import numpy as np 

def function(x):

	d9 = 1
	w7 = 5
	paths = []
	try:
		if w7 <= 8:
			w7 = 7+w7
			w7 = w7-1
			paths.append(1)
		else:
			x = x/4
			w7 = 4*x
			paths.append(2)
		if x < 6:
			x = 2+x
			paths.append(3)
		else:
			x = x+8
			w7 = w7*d9
			w7 = 1/w7
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