import numpy as np 

def function(x):

	t9 = 8
	w4 = 2
	paths = []
	try:
		if w4 <= 0:
			x = t9+x
			paths.append(1)
		else:
			w4 = 6*x
			t9 = 4-x
			paths.append(2)
		if w4 >= 5:
			t9 = t9-8
			w4 = 0+w4
			paths.append(3)
		else:
			w4 = 0+w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))