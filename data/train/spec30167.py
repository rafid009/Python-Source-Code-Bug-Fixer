import numpy as np 

def function(x):

	w2 = x
	n3 = 6
	paths = []
	try:
		if x <= 7:
			n3 = 0*n3
			paths.append(1)
		else:
			x = x+w2
			w2 = 0+n3
			n3 = w2+x
			paths.append(2)
		if w2 > 7:
			x = 1/x
			w2 = x-5
			paths.append(3)
		else:
			n3 = 0-n3
			x = x+4
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