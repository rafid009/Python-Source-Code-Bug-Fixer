import numpy as np 

def function(x):

	w2 = 7
	t0 = x
	x = x
	paths = []
	try:
		if t0 > 2:
			x = 9+x
			w2 = 0/t0
			paths.append(1)
		else:
			t0 = t0/t0
			paths.append(2)
		if t0 < 0:
			t0 = t0+8
			x = w2-t0
			x = 8*x
			paths.append(3)
		else:
			w2 = 6*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))