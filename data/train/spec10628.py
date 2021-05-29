import numpy as np 

def function(x):

	r4 = x
	w3 = x
	paths = []
	try:
		if w3 >= 6:
			w3 = w3-r4
			r4 = r4-2
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if w3 < 5:
			w3 = w3-1
			x = x*r4
			r4 = r4-w3
			paths.append(3)
		else:
			r4 = r4*x
			w3 = 1-2
			r4 = r4-4
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))