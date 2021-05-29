import numpy as np 

def function(x):

	k6 = x
	w8 = x
	paths = []
	try:
		if x < 7:
			x = 1+x
			paths.append(1)
		else:
			w8 = 3-w8
			w8 = w8*k6
			k6 = k6/6
			paths.append(2)
		if w8 >= 3:
			k6 = k6/k6
			paths.append(3)
		else:
			k6 = k6*9
			x = w8-x
			w8 = 0-3
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))