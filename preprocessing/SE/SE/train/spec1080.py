import numpy as np 

def function(x):

	w5 = x
	t0 = x
	paths = []
	try:
		if t0 <= 4:
			t0 = w5+t0
			paths.append(1)
		else:
			w5 = 9+w5
			w5 = 2*w5
			paths.append(2)
		if x > 6:
			t0 = 0-w5
			t0 = t0/2
			x = x+w5
			paths.append(3)
		else:
			w5 = x+w5
			x = x+0
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