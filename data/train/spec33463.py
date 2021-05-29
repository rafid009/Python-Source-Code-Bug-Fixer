import numpy as np 

def function(x):

	w3 = 8
	f5 = x
	paths = []
	try:
		if w3 >= 9:
			x = x-4
			paths.append(1)
		else:
			f5 = w3+w3
			w3 = 8*8
			x = 5/x
			paths.append(2)
		if f5 >= 6:
			x = 9/x
			f5 = 9-f5
			paths.append(3)
		else:
			x = 5/x
			x = 9+4
			f5 = f5+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))