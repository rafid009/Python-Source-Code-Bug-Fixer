import numpy as np 

def function(x):

	w3 = x
	r1 = 0
	x = 9
	paths = []
	try:
		if w3 < 1:
			r1 = x*w3
			paths.append(1)
		else:
			r1 = 2/9
			paths.append(2)
		if w3 >= 9:
			w3 = w3/7
			x = 5-6
			paths.append(3)
		else:
			w3 = w3/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))