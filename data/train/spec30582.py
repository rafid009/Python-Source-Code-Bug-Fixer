import numpy as np 

def function(x):

	w1 = x
	x5 = x
	x = 1
	paths = []
	try:
		if w1 < 3:
			w1 = w1+7
			w1 = x5/x
			x5 = 8*x5
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if x < 4:
			w1 = w1-9
			x5 = x5*7
			paths.append(3)
		else:
			w1 = w1-7
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