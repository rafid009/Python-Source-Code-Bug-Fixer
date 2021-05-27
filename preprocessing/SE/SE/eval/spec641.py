import numpy as np 

def function(x):

	f0 = 1
	w4 = x
	paths = []
	try:
		if x >= 7:
			f0 = f0+w4
			paths.append(1)
		else:
			f0 = 8*f0
			f0 = 6/f0
			paths.append(2)
		if f0 < 5:
			x = w4/x
			w4 = w4-8
			paths.append(3)
		else:
			w4 = w4+f0
			x = 5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))