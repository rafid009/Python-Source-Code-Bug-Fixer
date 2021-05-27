import numpy as np 

def function(x):

	t0 = 0
	w3 = x
	paths = []
	try:
		if t0 < 0:
			w3 = x/w3
			w3 = w3-0
			paths.append(1)
		else:
			x = x+w3
			w3 = 4-1
			paths.append(2)
		if w3 > 8:
			w3 = 8+w3
			paths.append(3)
		else:
			w3 = 0+w3
			t0 = t0*5
			w3 = 7+t0
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