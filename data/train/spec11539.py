import numpy as np 

def function(x):

	w4 = x
	d2 = 0
	paths = []
	try:
		if d2 >= 3:
			x = x+2
			paths.append(1)
		else:
			d2 = 0+d2
			paths.append(2)
		if w4 >= 9:
			x = x+8
			w4 = 2-w4
			x = d2/w4
			paths.append(3)
		else:
			x = x*9
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