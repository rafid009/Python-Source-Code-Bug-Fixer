import numpy as np 

def function(x):

	a2 = 0
	w4 = x
	paths = []
	try:
		if x < 2:
			x = 9*x
			paths.append(1)
		else:
			w4 = 9/7
			a2 = 1/7
			a2 = 3/9
			paths.append(2)
		if x > 5:
			x = 1/w4
			x = 0*w4
			paths.append(3)
		else:
			x = 3+5
			w4 = 9/3
			w4 = w4-5
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		a2 = w4**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))