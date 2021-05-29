import numpy as np 

def function(x):

	y7 = 1
	w3 = x
	paths = []
	try:
		if w3 <= 3:
			y7 = y7-w3
			paths.append(1)
		else:
			x = x/x
			x = 2*w3
			paths.append(2)
		if w3 >= 4:
			w3 = w3*2
			paths.append(3)
		else:
			x = w3+x
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