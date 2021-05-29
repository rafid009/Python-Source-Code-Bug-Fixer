import numpy as np 

def function(x):

	w0 = 0
	l7 = x
	paths = []
	try:
		if l7 >= 8:
			x = x+l7
			x = x+3
			paths.append(1)
		else:
			x = x*x
			l7 = l7-2
			l7 = 6*l7
			paths.append(2)
		if l7 >= 3:
			x = l7+4
			x = 3+w0
			paths.append(3)
		else:
			w0 = w0/l7
			x = 8/x
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