import numpy as np 

def function(x):

	y2 = x
	w2 = 2
	paths = []
	try:
		if w2 < 1:
			y2 = y2+x
			paths.append(1)
		else:
			x = 9+x
			w2 = w2/9
			x = x+x
			paths.append(2)
		if y2 < 8:
			w2 = w2-9
			w2 = w2/x
			paths.append(3)
		else:
			y2 = y2/3
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