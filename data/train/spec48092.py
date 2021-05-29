import numpy as np 

def function(x):

	a6 = 5
	w1 = 5
	paths = []
	try:
		if w1 > 2:
			w1 = 9-9
			w1 = 1*w1
			w1 = a6-9
			paths.append(1)
		else:
			a6 = x*a6
			w1 = w1-3
			x = x*a6
			paths.append(2)
		if a6 < 0:
			a6 = 7+a6
			w1 = w1+2
			paths.append(3)
		else:
			a6 = w1/7
			w1 = 3-w1
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))