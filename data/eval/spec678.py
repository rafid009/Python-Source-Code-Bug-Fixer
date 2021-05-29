import numpy as np 

def function(x):

	a5 = x
	w6 = 5
	paths = []
	try:
		if w6 > 5:
			w6 = 3-w6
			x = x+7
			paths.append(1)
		else:
			x = a5-9
			paths.append(2)
		if a5 < 7:
			x = x-a5
			a5 = 5+a5
			paths.append(3)
		else:
			w6 = 0-3
			x = x-x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))