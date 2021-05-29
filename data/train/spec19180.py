import numpy as np 

def function(x):

	w7 = x
	f8 = 9
	x = x
	paths = []
	try:
		if w7 >= 3:
			f8 = 7+f8
			paths.append(1)
		else:
			w7 = f8+w7
			paths.append(2)
		if w7 <= 2:
			x = x/x
			f8 = 5+f8
			paths.append(3)
		else:
			f8 = f8-w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		x = w7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))