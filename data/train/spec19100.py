import numpy as np 

def function(x):

	f4 = x
	w9 = 2
	paths = []
	try:
		if x >= 1:
			f4 = 5+f4
			w9 = w9*x
			paths.append(1)
		else:
			w9 = 3-w9
			x = 7-w9
			paths.append(2)
		if x >= 7:
			f4 = 9+f4
			paths.append(3)
		else:
			x = 0/f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))