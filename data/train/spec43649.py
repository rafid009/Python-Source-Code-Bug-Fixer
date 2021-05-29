import numpy as np 

def function(x):

	a5 = x
	w4 = x
	paths = []
	try:
		if a5 <= 3:
			w4 = w4+0
			x = 8+x
			x = 7+a5
			paths.append(1)
		else:
			x = 3-x
			a5 = a5+x
			w4 = a5/w4
			paths.append(2)
		if x <= 7:
			x = x*5
			a5 = x*7
			a5 = 6*w4
			paths.append(3)
		else:
			x = 5+a5
			x = 2*8
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