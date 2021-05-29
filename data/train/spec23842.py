import numpy as np 

def function(x):

	w1 = x
	l6 = x
	paths = []
	try:
		if l6 > 8:
			w1 = 7-3
			w1 = w1/l6
			paths.append(1)
		else:
			w1 = 2*w1
			w1 = 0-w1
			x = l6*8
			paths.append(2)
		if l6 >= 2:
			w1 = 0-w1
			w1 = w1/w1
			paths.append(3)
		else:
			x = w1+x
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))