import numpy as np 

def function(x):

	w2 = 7
	k2 = 1
	paths = []
	try:
		if w2 > 8:
			k2 = k2/k2
			paths.append(1)
		else:
			w2 = w2/1
			paths.append(2)
		if x < 9:
			k2 = k2/1
			k2 = 2-w2
			paths.append(3)
		else:
			w2 = 3-x
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