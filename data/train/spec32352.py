import numpy as np 

def function(x):

	x9 = x
	w2 = x
	paths = []
	try:
		if w2 > 6:
			w2 = w2*2
			x = x9/x
			w2 = 2*w2
			paths.append(1)
		else:
			x9 = x9-w2
			x = 9+6
			paths.append(2)
		if w2 <= 1:
			x = 2+w2
			x = w2/x
			paths.append(3)
		else:
			x9 = x9-0
			x9 = x9-w2
			w2 = 0*w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))