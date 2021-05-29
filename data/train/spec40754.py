import numpy as np 

def function(x):

	w0 = x
	b8 = x
	x = 5
	paths = []
	try:
		if b8 < 2:
			w0 = 5+w0
			paths.append(1)
		else:
			b8 = 4-3
			b8 = b8/6
			b8 = 9-b8
			paths.append(2)
		if x > 0:
			w0 = 0+x
			paths.append(3)
		else:
			w0 = w0/6
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))