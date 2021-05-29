import numpy as np 

def function(x):

	w8 = x
	x3 = x
	paths = []
	try:
		if w8 <= 8:
			w8 = w8-2
			paths.append(1)
		else:
			x3 = x3*w8
			x3 = x3+x3
			paths.append(2)
		if x <= 4:
			x = 6+2
			paths.append(3)
		else:
			x = x3-x
			x = 7*x3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		w8 = x3**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))