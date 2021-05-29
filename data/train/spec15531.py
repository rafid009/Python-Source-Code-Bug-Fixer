import numpy as np 

def function(x):

	x3 = 7
	w6 = 2
	paths = []
	try:
		if w6 < 2:
			w6 = x3*3
			x = 4+x
			x3 = 2-x
			paths.append(1)
		else:
			w6 = 3/w6
			x3 = 5*5
			paths.append(2)
		if x > 6:
			x3 = x3/4
			x3 = 3*x3
			paths.append(3)
		else:
			x3 = x/x3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))