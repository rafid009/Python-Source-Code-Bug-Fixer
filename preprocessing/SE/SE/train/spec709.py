import numpy as np 

def function(x):

	w6 = 8
	n5 = 9
	paths = []
	try:
		if n5 <= 0:
			n5 = 2/6
			n5 = n5-w6
			paths.append(1)
		else:
			w6 = w6-4
			paths.append(2)
		if w6 > 7:
			n5 = 9-n5
			x = n5-x
			x = n5/w6
			paths.append(3)
		else:
			n5 = w6-9
			n5 = n5-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))