import numpy as np 

def function(x):

	w4 = x
	p1 = 4
	paths = []
	try:
		if w4 > 1:
			x = x*1
			x = w4/x
			w4 = w4-1
			paths.append(1)
		else:
			w4 = 5+x
			p1 = p1-9
			w4 = 3-w4
			paths.append(2)
		if w4 >= 8:
			w4 = w4+3
			w4 = 6*w4
			paths.append(3)
		else:
			x = x*p1
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))