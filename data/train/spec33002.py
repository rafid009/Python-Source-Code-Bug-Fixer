import numpy as np 

def function(x):

	w4 = 2
	i8 = 5
	paths = []
	try:
		if i8 < 9:
			i8 = w4*w4
			paths.append(1)
		else:
			w4 = w4-1
			x = 8+x
			paths.append(2)
		if w4 < 2:
			i8 = 4*x
			x = 2*2
			w4 = i8/5
			paths.append(3)
		else:
			w4 = 8-3
			w4 = i8/w4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))