import numpy as np 

def function(x):

	w8 = 6
	x7 = x
	paths = []
	try:
		if w8 >= 7:
			w8 = 2-x
			x = x/5
			paths.append(1)
		else:
			x = x/1
			x7 = x7*9
			paths.append(2)
		if x7 <= 8:
			w8 = 6+w8
			x = x*7
			paths.append(3)
		else:
			w8 = w8/x7
			x7 = 8*9
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))