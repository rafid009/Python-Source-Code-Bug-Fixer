import numpy as np 

def function(x):

	w8 = x
	t2 = 1
	paths = []
	try:
		if t2 > 6:
			t2 = t2*8
			w8 = w8*w8
			paths.append(1)
		else:
			x = 8*5
			t2 = t2*t2
			w8 = w8/4
			paths.append(2)
		if w8 >= 6:
			w8 = w8*9
			x = 6-x
			t2 = 1-w8
			paths.append(3)
		else:
			w8 = w8+w8
			x = x-t2
			t2 = t2+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))