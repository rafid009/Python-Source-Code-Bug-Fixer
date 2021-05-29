import numpy as np 

def function(x):

	w9 = 3
	q5 = 5
	paths = []
	try:
		if x <= 8:
			q5 = x-2
			paths.append(1)
		else:
			w9 = w9-6
			paths.append(2)
		if w9 >= 1:
			w9 = w9*x
			x = x*4
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))