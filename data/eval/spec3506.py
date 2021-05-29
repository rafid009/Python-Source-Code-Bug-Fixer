import numpy as np 

def function(x):

	t4 = x
	w9 = 3
	paths = []
	try:
		if x >= 6:
			w9 = 0*w9
			paths.append(1)
		else:
			w9 = 6*5
			paths.append(2)
		if x >= 1:
			x = 2-5
			t4 = t4+w9
			paths.append(3)
		else:
			x = w9+x
			t4 = t4-9
			t4 = 2+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))