import numpy as np 

def function(x):

	w9 = x
	i9 = 5
	paths = []
	try:
		if x > 5:
			x = 4/x
			x = 9/7
			paths.append(1)
		else:
			i9 = i9/1
			w9 = 8/1
			paths.append(2)
		if w9 < 7:
			i9 = i9/5
			paths.append(3)
		else:
			i9 = i9+i9
			w9 = w9-4
			x = i9/x
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