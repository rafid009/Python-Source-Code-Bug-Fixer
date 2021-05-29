import numpy as np 

def function(x):

	w1 = 1
	w0 = 4
	paths = []
	try:
		if x > 1:
			w0 = w0*9
			x = 3+w1
			paths.append(1)
		else:
			w1 = 2*5
			w1 = x+x
			paths.append(2)
		if x <= 6:
			x = x-0
			paths.append(3)
		else:
			w0 = 2-w0
			w1 = w0+w1
			w0 = 6/3
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