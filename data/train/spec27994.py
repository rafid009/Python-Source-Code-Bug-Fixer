import numpy as np 

def function(x):

	w1 = 3
	x5 = x
	paths = []
	try:
		if x5 > 1:
			x = x5*2
			x = x/x5
			x5 = x5*w1
			paths.append(1)
		else:
			w1 = 7*w1
			paths.append(2)
		if w1 < 6:
			x = x5*x
			paths.append(3)
		else:
			x = x/7
			w1 = w1*w1
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