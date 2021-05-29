import numpy as np 

def function(x):

	w9 = 5
	i2 = 5
	paths = []
	try:
		if i2 >= 7:
			x = 6/x
			w9 = w9*1
			paths.append(1)
		else:
			w9 = w9/w9
			paths.append(2)
		if x >= 0:
			x = x/i2
			w9 = 1-6
			paths.append(3)
		else:
			w9 = 5+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))