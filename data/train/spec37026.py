import numpy as np 

def function(x):

	f1 = 5
	w8 = 2
	paths = []
	try:
		if f1 < 3:
			x = 1-x
			paths.append(1)
		else:
			f1 = w8*3
			f1 = 8+7
			paths.append(2)
		if w8 < 0:
			x = x*7
			w8 = w8*0
			w8 = f1*f1
			paths.append(3)
		else:
			w8 = 1/w8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))