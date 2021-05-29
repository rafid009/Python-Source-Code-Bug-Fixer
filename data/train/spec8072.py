import numpy as np 

def function(x):

	w8 = 8
	n9 = 7
	paths = []
	try:
		if n9 < 6:
			w8 = 0-x
			x = n9-x
			w8 = w8/8
			paths.append(1)
		else:
			n9 = n9*n9
			n9 = w8-9
			paths.append(2)
		if x > 0:
			w8 = 1*1
			w8 = w8-w8
			x = 1+1
			paths.append(3)
		else:
			w8 = w8/3
			w8 = w8*x
			x = x+1
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