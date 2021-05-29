import numpy as np 

def function(x):

	w8 = x
	t8 = x
	paths = []
	try:
		if t8 <= 7:
			t8 = x*8
			t8 = 9+t8
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if w8 <= 1:
			t8 = t8+3
			t8 = x/x
			paths.append(3)
		else:
			w8 = w8-0
			x = 4/x
			w8 = t8+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))