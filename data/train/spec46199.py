import numpy as np 

def function(x):

	t3 = x
	w0 = x
	paths = []
	try:
		if x > 4:
			t3 = w0/4
			w0 = w0*3
			paths.append(1)
		else:
			x = 8*x
			w0 = 6*w0
			t3 = x-5
			paths.append(2)
		if w0 >= 1:
			x = x/9
			w0 = w0-t3
			paths.append(3)
		else:
			t3 = 6+0
			t3 = 6+t3
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