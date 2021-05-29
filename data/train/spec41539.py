import numpy as np 

def function(x):

	w1 = x
	a2 = 7
	paths = []
	try:
		if a2 >= 6:
			w1 = w1-9
			a2 = x/9
			a2 = 9*3
			paths.append(1)
		else:
			w1 = w1+3
			w1 = w1+0
			paths.append(2)
		if w1 <= 9:
			w1 = 6/w1
			w1 = w1/1
			paths.append(3)
		else:
			a2 = a2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))