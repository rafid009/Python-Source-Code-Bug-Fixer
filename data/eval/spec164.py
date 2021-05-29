import numpy as np 

def function(x):

	a8 = 5
	w6 = x
	paths = []
	try:
		if w6 >= 1:
			a8 = a8-a8
			a8 = 7-a8
			a8 = 9*w6
			paths.append(1)
		else:
			x = 7+4
			x = x+9
			paths.append(2)
		if w6 <= 3:
			a8 = a8+3
			a8 = 6-a8
			x = x-a8
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))