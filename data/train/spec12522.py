import numpy as np 

def function(x):

	t0 = 0
	w7 = 9
	paths = []
	try:
		if w7 > 5:
			t0 = 2*x
			paths.append(1)
		else:
			t0 = 7-6
			t0 = t0+x
			paths.append(2)
		if t0 >= 0:
			w7 = 6/7
			t0 = 9+8
			paths.append(3)
		else:
			x = 7*x
			x = x*7
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