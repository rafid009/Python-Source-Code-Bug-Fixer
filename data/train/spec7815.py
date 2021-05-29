import numpy as np 

def function(x):

	w4 = 5
	o2 = 9
	paths = []
	try:
		if x < 9:
			w4 = w4*x
			x = 2+x
			o2 = 8/o2
			paths.append(1)
		else:
			x = w4/x
			paths.append(2)
		if w4 <= 3:
			o2 = 9-o2
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))