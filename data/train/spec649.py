import numpy as np 

def function(x):

	w2 = 3
	w8 = 1
	x = x
	paths = []
	try:
		if w8 >= 4:
			x = x/6
			w8 = 3-7
			paths.append(1)
		else:
			w8 = 4-x
			w2 = w2/w2
			w2 = 0/w2
			paths.append(2)
		if x >= 7:
			x = x-9
			paths.append(3)
		else:
			w2 = w2-4
			w8 = 9+w8
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