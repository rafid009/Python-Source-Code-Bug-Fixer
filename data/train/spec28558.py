import numpy as np 

def function(x):

	x1 = x
	w6 = x
	paths = []
	try:
		if w6 > 9:
			w6 = w6+0
			paths.append(1)
		else:
			x1 = 3*9
			paths.append(2)
		if x < 9:
			w6 = 9/w6
			x = x-7
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))