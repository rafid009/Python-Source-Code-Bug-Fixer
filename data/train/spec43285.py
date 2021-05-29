import numpy as np 

def function(x):

	w0 = x
	t2 = x
	paths = []
	try:
		if w0 <= 3:
			x = 9/5
			paths.append(1)
		else:
			w0 = t2/5
			paths.append(2)
		if w0 > 0:
			w0 = w0+8
			t2 = t2-6
			t2 = t2+x
			paths.append(3)
		else:
			x = 3/x
			x = 8/x
			x = x+3
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))