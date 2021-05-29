import numpy as np 

def function(x):

	n8 = 8
	w2 = 0
	paths = []
	try:
		if n8 <= 8:
			w2 = w2/8
			paths.append(1)
		else:
			n8 = 1/n8
			n8 = 7-n8
			w2 = x+x
			paths.append(2)
		if n8 > 3:
			w2 = w2-3
			paths.append(3)
		else:
			n8 = 1/8
			w2 = 4/w2
			n8 = 8-n8
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