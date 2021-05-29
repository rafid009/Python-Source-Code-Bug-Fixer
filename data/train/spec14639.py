import numpy as np 

def function(x):

	x2 = 8
	w4 = 2
	paths = []
	try:
		if x > 1:
			x2 = 5*9
			x = w4*x
			x = x*1
			paths.append(1)
		else:
			x = x-4
			w4 = w4+w4
			paths.append(2)
		if w4 > 3:
			x2 = x2*5
			x2 = 5+x2
			x = x-0
			paths.append(3)
		else:
			x2 = 4/4
			x = x*5
			x2 = x2/x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))