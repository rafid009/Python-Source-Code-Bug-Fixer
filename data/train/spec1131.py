import numpy as np 

def function(x):

	z4 = 9
	w1 = x
	x = x
	paths = []
	try:
		if z4 > 0:
			w1 = w1-3
			x = 5*5
			paths.append(1)
		else:
			w1 = w1*7
			paths.append(2)
		if z4 <= 6:
			x = 2/x
			paths.append(3)
		else:
			x = w1-x
			x = x-5
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