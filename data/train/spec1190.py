import numpy as np 

def function(x):

	l7 = x
	w0 = x
	x = 1
	paths = []
	try:
		if w0 > 8:
			w0 = w0*6
			x = 1+x
			l7 = 8/2
			paths.append(1)
		else:
			l7 = l7+4
			x = 5-w0
			paths.append(2)
		if w0 >= 5:
			x = 3+0
			w0 = w0*4
			paths.append(3)
		else:
			l7 = l7*w0
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		w0 = l7**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))