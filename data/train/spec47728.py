import numpy as np 

def function(x):

	w7 = 9
	w3 = 2
	paths = []
	try:
		if w3 > 4:
			x = 0+6
			x = x-x
			w3 = w3+3
			paths.append(1)
		else:
			w7 = w3/w7
			w7 = x/x
			paths.append(2)
		if w7 <= 2:
			x = x+5
			paths.append(3)
		else:
			x = 7*x
			w3 = 6-5
			w7 = w7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))