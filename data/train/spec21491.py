import numpy as np 

def function(x):

	x3 = 2
	w7 = x
	paths = []
	try:
		if x3 <= 2:
			w7 = 6-w7
			x = 5-8
			paths.append(1)
		else:
			x = x3-w7
			paths.append(2)
		if w7 <= 2:
			x3 = x3*5
			paths.append(3)
		else:
			w7 = 7-8
			w7 = w7*2
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))