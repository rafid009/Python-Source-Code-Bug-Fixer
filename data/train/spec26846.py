import numpy as np 

def function(x):

	w7 = 0
	v0 = x
	paths = []
	try:
		if x >= 8:
			v0 = 0-9
			x = 7-x
			w7 = v0*2
			paths.append(1)
		else:
			x = 9*x
			w7 = 6/x
			paths.append(2)
		if x <= 5:
			w7 = w7*6
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))