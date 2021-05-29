import numpy as np 

def function(x):

	a8 = 5
	w6 = 7
	paths = []
	try:
		if x >= 7:
			w6 = x+3
			a8 = 6*a8
			paths.append(1)
		else:
			x = x+9
			a8 = a8*3
			paths.append(2)
		if a8 < 2:
			a8 = w6-a8
			a8 = a8/8
			paths.append(3)
		else:
			a8 = 8+8
			a8 = w6-1
			w6 = 8-w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		a8 = w6**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))