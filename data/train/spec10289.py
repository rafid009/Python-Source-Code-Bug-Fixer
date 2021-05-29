import numpy as np 

def function(x):

	w7 = x
	a4 = x
	paths = []
	try:
		if x > 2:
			x = 4*5
			a4 = 8-1
			paths.append(1)
		else:
			a4 = a4/4
			x = x-x
			paths.append(2)
		if w7 < 7:
			w7 = w7+a4
			a4 = a4-1
			x = 4+x
			paths.append(3)
		else:
			w7 = 4/a4
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