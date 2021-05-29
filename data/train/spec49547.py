import numpy as np 

def function(x):

	w0 = 9
	n3 = 2
	paths = []
	try:
		if n3 <= 8:
			n3 = n3+0
			x = x-9
			w0 = w0/9
			paths.append(1)
		else:
			x = x+0
			n3 = 7*n3
			x = n3/x
			paths.append(2)
		if x < 8:
			w0 = x/5
			n3 = x+2
			paths.append(3)
		else:
			w0 = 2-w0
			w0 = 2-9
			n3 = n3-4
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		w0 = w0**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))