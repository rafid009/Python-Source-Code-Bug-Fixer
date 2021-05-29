import numpy as np 

def function(x):

	b4 = x
	w4 = x
	paths = []
	try:
		if x > 4:
			w4 = w4+5
			paths.append(1)
		else:
			b4 = b4-3
			paths.append(2)
		if w4 < 5:
			x = 7+6
			x = x-8
			x = b4-x
			paths.append(3)
		else:
			w4 = w4+8
			b4 = 3-b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))