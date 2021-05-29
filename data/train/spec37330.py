import numpy as np 

def function(x):

	w9 = 5
	e8 = x
	paths = []
	try:
		if x >= 3:
			x = 8-5
			x = w9-7
			w9 = e8-1
			paths.append(1)
		else:
			w9 = x/x
			e8 = e8+7
			paths.append(2)
		if x < 0:
			w9 = 8-w9
			x = 0+x
			e8 = 9*w9
			paths.append(3)
		else:
			w9 = 6*w9
			w9 = e8/5
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		w9 = e8**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))