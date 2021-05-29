import numpy as np 

def function(x):

	w5 = 8
	n6 = x
	x = 3
	paths = []
	try:
		if w5 <= 1:
			n6 = n6*6
			w5 = 1*w5
			w5 = 6-w5
			paths.append(1)
		else:
			w5 = 2+6
			n6 = n6-2
			w5 = x+n6
			paths.append(2)
		if w5 >= 6:
			x = 9-x
			n6 = n6*7
			w5 = w5+w5
			paths.append(3)
		else:
			n6 = n6*w5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))