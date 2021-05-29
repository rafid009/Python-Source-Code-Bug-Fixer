import numpy as np 

def function(x):

	w2 = x
	w9 = 3
	paths = []
	try:
		if x >= 7:
			w2 = 1*w2
			paths.append(1)
		else:
			w2 = w2-6
			paths.append(2)
		if w2 > 2:
			w9 = x-7
			w2 = 3-5
			w2 = 0-w2
			paths.append(3)
		else:
			x = 8/x
			w9 = 3*2
			x = x+0
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))