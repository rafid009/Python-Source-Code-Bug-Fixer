import numpy as np 

def function(x):

	w5 = 4
	n5 = x
	x = x
	paths = []
	try:
		if n5 >= 8:
			x = x/x
			paths.append(1)
		else:
			x = 1*x
			w5 = w5*w5
			paths.append(2)
		if w5 <= 0:
			x = x-n5
			x = n5*3
			paths.append(3)
		else:
			w5 = 6+9
			n5 = n5-n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))