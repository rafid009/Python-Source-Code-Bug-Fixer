import numpy as np 

def function(x):

	w2 = 1
	l2 = x
	paths = []
	try:
		if x >= 1:
			l2 = 3/l2
			w2 = w2-5
			paths.append(1)
		else:
			w2 = 7/w2
			l2 = w2/2
			paths.append(2)
		if w2 > 6:
			w2 = w2+w2
			paths.append(3)
		else:
			w2 = w2-w2
			x = x+x
			w2 = w2*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))