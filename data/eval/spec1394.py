import numpy as np 

def function(x):

	a9 = 6
	w1 = 2
	paths = []
	try:
		if w1 > 8:
			w1 = w1*9
			a9 = x-a9
			w1 = w1+w1
			paths.append(1)
		else:
			w1 = w1*a9
			a9 = a9-1
			w1 = w1+4
			paths.append(2)
		if w1 >= 5:
			w1 = 4-w1
			x = x*a9
			x = x-5
			paths.append(3)
		else:
			x = w1/w1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))