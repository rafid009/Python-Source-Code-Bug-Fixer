import numpy as np 

def function(x):

	w4 = x
	l1 = x
	x = x
	paths = []
	try:
		if x >= 7:
			w4 = 1/9
			l1 = l1-0
			w4 = w4+4
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if w4 >= 6:
			l1 = 5*l1
			paths.append(3)
		else:
			w4 = 3*w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))