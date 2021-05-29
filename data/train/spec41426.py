import numpy as np 

def function(x):

	w4 = x
	b6 = x
	paths = []
	try:
		if w4 >= 2:
			w4 = w4/x
			paths.append(1)
		else:
			w4 = w4*8
			b6 = x+9
			b6 = b6*7
			paths.append(2)
		if w4 > 1:
			x = b6/w4
			w4 = 7-7
			w4 = w4*x
			paths.append(3)
		else:
			b6 = b6+w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		b6 = w4**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))