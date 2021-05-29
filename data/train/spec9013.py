import numpy as np 

def function(x):

	a6 = x
	w1 = x
	paths = []
	try:
		if w1 > 7:
			a6 = 5*a6
			x = x-a6
			paths.append(1)
		else:
			a6 = 6+a6
			a6 = 9-3
			paths.append(2)
		if a6 < 1:
			w1 = w1-9
			w1 = 9*1
			paths.append(3)
		else:
			a6 = a6-w1
			a6 = a6/5
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))