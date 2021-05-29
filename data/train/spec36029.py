import numpy as np 

def function(x):

	j6 = 0
	w9 = x
	paths = []
	try:
		if w9 >= 5:
			j6 = 8*w9
			x = j6*x
			w9 = 4-w9
			paths.append(1)
		else:
			x = 7-0
			x = 0-x
			w9 = w9+7
			paths.append(2)
		if j6 > 4:
			x = x+4
			j6 = j6-8
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))