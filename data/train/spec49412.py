import numpy as np 

def function(x):

	w8 = 3
	t3 = 1
	paths = []
	try:
		if x <= 3:
			x = x*6
			w8 = 5*4
			paths.append(1)
		else:
			x = 8*t3
			paths.append(2)
		if t3 <= 3:
			t3 = t3-t3
			w8 = 0/w8
			x = x+8
			paths.append(3)
		else:
			x = w8/x
			w8 = 5/w8
			t3 = x-w8
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