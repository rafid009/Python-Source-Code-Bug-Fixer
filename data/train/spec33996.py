import numpy as np 

def function(x):

	w2 = x
	d4 = 3
	paths = []
	try:
		if w2 < 2:
			d4 = 5/w2
			d4 = d4+x
			x = 6/7
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if w2 <= 2:
			w2 = 9/w2
			w2 = 2-w2
			paths.append(3)
		else:
			d4 = d4-4
			w2 = w2*6
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		w2 = d4**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))