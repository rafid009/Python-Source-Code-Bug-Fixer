import numpy as np 

def function(x):

	w2 = x
	w8 = x
	paths = []
	try:
		if x < 4:
			w8 = 1-w2
			x = x/w8
			paths.append(1)
		else:
			w8 = 7+w8
			w8 = w2*w2
			paths.append(2)
		if w2 >= 5:
			w8 = 6+w8
			w2 = 4/w2
			paths.append(3)
		else:
			w2 = w8-w2
			w8 = 5+w8
			w2 = w2-0
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w8 = w2**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))