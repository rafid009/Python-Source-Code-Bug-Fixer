import numpy as np 

def function(x):

	w8 = 8
	w2 = 0
	paths = []
	try:
		if x >= 2:
			w8 = w8-2
			x = x+x
			paths.append(1)
		else:
			w8 = w8*8
			w8 = 6/4
			paths.append(2)
		if w8 <= 7:
			w2 = 3+w2
			w2 = w2*5
			w2 = w2/4
			paths.append(3)
		else:
			w2 = w2*0
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