import numpy as np 

def function(x):

	w1 = 8
	v4 = 4
	paths = []
	try:
		if v4 > 9:
			v4 = 2+1
			x = x+4
			paths.append(1)
		else:
			w1 = 7-1
			v4 = w1-v4
			paths.append(2)
		if w1 < 4:
			v4 = 5+7
			w1 = 9-1
			w1 = 2-w1
			paths.append(3)
		else:
			x = x*4
			v4 = 1-v4
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