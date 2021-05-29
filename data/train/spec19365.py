import numpy as np 

def function(x):

	f8 = 4
	w4 = 0
	paths = []
	try:
		if w4 <= 6:
			x = x+8
			f8 = 3-1
			paths.append(1)
		else:
			f8 = w4-0
			x = 1*w4
			paths.append(2)
		if f8 <= 5:
			x = x/3
			f8 = 1*f8
			x = 8-x
			paths.append(3)
		else:
			w4 = 9-9
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))