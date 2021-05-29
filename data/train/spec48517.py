import numpy as np 

def function(x):

	f4 = 1
	w7 = x
	paths = []
	try:
		if x <= 1:
			w7 = 2-9
			paths.append(1)
		else:
			f4 = f4/3
			paths.append(2)
		if w7 > 1:
			w7 = w7-2
			paths.append(3)
		else:
			f4 = w7-w7
			f4 = x-4
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))