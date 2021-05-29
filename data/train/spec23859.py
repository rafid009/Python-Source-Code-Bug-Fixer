import numpy as np 

def function(x):

	w8 = 5
	q3 = x
	x = 5
	paths = []
	try:
		if q3 >= 6:
			x = 6+0
			x = x*x
			w8 = 3/w8
			paths.append(1)
		else:
			w8 = q3-w8
			w8 = 0/7
			w8 = q3+2
			paths.append(2)
		if w8 >= 6:
			w8 = w8*w8
			w8 = 4*w8
			q3 = q3/5
			paths.append(3)
		else:
			x = w8-w8
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))