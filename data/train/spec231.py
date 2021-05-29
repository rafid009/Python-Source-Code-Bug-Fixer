import numpy as np 

def function(x):

	w7 = 4
	v2 = x
	paths = []
	try:
		if v2 >= 0:
			w7 = 2-w7
			paths.append(1)
		else:
			w7 = w7/x
			w7 = 6-6
			paths.append(2)
		if w7 < 3:
			w7 = w7*x
			v2 = 1/v2
			v2 = x/3
			paths.append(3)
		else:
			w7 = 5-8
			w7 = w7-3
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		v2 = w7**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))