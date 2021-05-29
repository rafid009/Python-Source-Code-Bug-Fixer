import numpy as np 

def function(x):

	b2 = x
	w8 = x
	paths = []
	try:
		if w8 > 3:
			x = 2/7
			paths.append(1)
		else:
			w8 = 9+w8
			paths.append(2)
		if b2 < 6:
			x = x/w8
			paths.append(3)
		else:
			x = x+8
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))