import numpy as np 

def function(x):

	w1 = 7
	l0 = x
	paths = []
	try:
		if w1 > 8:
			x = x-w1
			l0 = l0/l0
			paths.append(1)
		else:
			w1 = w1-8
			l0 = l0/9
			paths.append(2)
		if w1 >= 2:
			x = 8+x
			paths.append(3)
		else:
			l0 = x+5
			w1 = 7/2
			x = x/3
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