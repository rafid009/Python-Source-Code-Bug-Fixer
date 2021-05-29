import numpy as np 

def function(x):

	w6 = x
	a6 = x
	x = 5
	paths = []
	try:
		if w6 >= 2:
			w6 = w6*w6
			paths.append(1)
		else:
			a6 = w6*5
			paths.append(2)
		if a6 >= 2:
			x = x+4
			w6 = 6*w6
			paths.append(3)
		else:
			w6 = 0+a6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))