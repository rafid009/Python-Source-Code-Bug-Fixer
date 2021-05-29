import numpy as np 

def function(x):

	l7 = 6
	w8 = 3
	paths = []
	try:
		if x < 0:
			w8 = w8-2
			x = 8*x
			l7 = l7/6
			paths.append(1)
		else:
			l7 = l7-8
			paths.append(2)
		if l7 < 8:
			w8 = 6*w8
			paths.append(3)
		else:
			l7 = 0+x
			x = 6*x
			l7 = 0+l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		w8 = l7**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))