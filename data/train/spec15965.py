import numpy as np 

def function(x):

	w8 = x
	l2 = 8
	x = 9
	paths = []
	try:
		if w8 < 0:
			w8 = w8*9
			w8 = w8-w8
			paths.append(1)
		else:
			x = x/w8
			paths.append(2)
		if x >= 1:
			w8 = w8-4
			l2 = 1-l2
			paths.append(3)
		else:
			x = x*w8
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))