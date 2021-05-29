import numpy as np 

def function(x):

	w6 = x
	a4 = x
	paths = []
	try:
		if x >= 9:
			x = 9-w6
			paths.append(1)
		else:
			a4 = w6*6
			w6 = 5*w6
			a4 = 7/a4
			paths.append(2)
		if a4 > 1:
			a4 = a4-a4
			x = a4/x
			a4 = a4/9
			paths.append(3)
		else:
			x = x*w6
			w6 = 6/w6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))