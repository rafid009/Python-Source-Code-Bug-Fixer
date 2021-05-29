import numpy as np 

def function(x):

	x9 = 2
	w6 = 9
	paths = []
	try:
		if w6 > 5:
			w6 = x*w6
			x9 = x9-3
			w6 = w6-7
			paths.append(1)
		else:
			w6 = w6/1
			x = x9/x9
			w6 = w6*x9
			paths.append(2)
		if x >= 9:
			x9 = 2*2
			x = x+7
			paths.append(3)
		else:
			w6 = x-2
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