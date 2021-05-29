import numpy as np 

def function(x):

	j6 = 7
	w6 = x
	paths = []
	try:
		if j6 < 1:
			w6 = j6*9
			x = x/4
			paths.append(1)
		else:
			w6 = w6/9
			w6 = w6*w6
			paths.append(2)
		if j6 < 8:
			x = x+3
			x = w6-3
			paths.append(3)
		else:
			x = x-1
			w6 = j6-w6
			w6 = 9/w6
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