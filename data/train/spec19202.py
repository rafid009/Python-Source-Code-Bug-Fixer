import numpy as np 

def function(x):

	w5 = x
	n5 = 1
	paths = []
	try:
		if w5 < 9:
			x = x-9
			paths.append(1)
		else:
			n5 = 6+n5
			n5 = n5/w5
			paths.append(2)
		if x >= 3:
			n5 = n5*4
			w5 = 2-w5
			w5 = w5/2
			paths.append(3)
		else:
			x = n5/4
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