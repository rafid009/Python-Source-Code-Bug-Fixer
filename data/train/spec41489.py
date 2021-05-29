import numpy as np 

def function(x):

	r2 = 6
	w1 = 3
	paths = []
	try:
		if r2 >= 6:
			w1 = 9+w1
			r2 = 7*x
			w1 = w1/w1
			paths.append(1)
		else:
			w1 = w1+r2
			w1 = x/1
			x = 3+x
			paths.append(2)
		if w1 > 6:
			x = 2*r2
			paths.append(3)
		else:
			w1 = w1*3
			x = w1/x
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