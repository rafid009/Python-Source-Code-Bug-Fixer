import numpy as np 

def function(x):

	w1 = 2
	x6 = 5
	paths = []
	try:
		if x6 >= 7:
			x6 = x6/x6
			w1 = w1/w1
			paths.append(1)
		else:
			w1 = w1+2
			w1 = 3-8
			x = w1-x
			paths.append(2)
		if x6 >= 8:
			w1 = w1-8
			paths.append(3)
		else:
			x6 = w1*x6
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