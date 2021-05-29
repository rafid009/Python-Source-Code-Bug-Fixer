import numpy as np 

def function(x):

	w8 = 1
	x7 = x
	paths = []
	try:
		if w8 > 4:
			x = x+x
			paths.append(1)
		else:
			x = 3/x7
			w8 = x/7
			paths.append(2)
		if x7 <= 0:
			x7 = w8*1
			paths.append(3)
		else:
			x = x/5
			w8 = 3+w8
			x7 = x7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))