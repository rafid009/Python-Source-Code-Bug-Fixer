import numpy as np 

def function(x):

	x2 = 7
	w6 = 4
	paths = []
	try:
		if x2 > 8:
			w6 = 2*9
			x2 = x2-6
			paths.append(1)
		else:
			w6 = 5/x
			paths.append(2)
		if w6 >= 6:
			x2 = x2-0
			x = x-5
			x2 = 8+9
			paths.append(3)
		else:
			w6 = w6/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))