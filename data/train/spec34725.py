import numpy as np 

def function(x):

	w7 = 1
	w6 = 9
	paths = []
	try:
		if w6 < 3:
			w7 = 2/w7
			paths.append(1)
		else:
			w7 = w7-w6
			paths.append(2)
		if w6 >= 5:
			x = x-9
			w6 = 0+7
			w6 = w6/9
			paths.append(3)
		else:
			x = x*2
			x = x-9
			w6 = 4-w7
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