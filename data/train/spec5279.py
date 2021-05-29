import numpy as np 

def function(x):

	w0 = 8
	t7 = x
	paths = []
	try:
		if t7 >= 9:
			t7 = t7/x
			paths.append(1)
		else:
			t7 = x/5
			x = x-8
			w0 = 3/w0
			paths.append(2)
		if w0 >= 0:
			w0 = w0-7
			t7 = 7+1
			t7 = t7-x
			paths.append(3)
		else:
			t7 = 1-t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))