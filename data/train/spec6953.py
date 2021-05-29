import numpy as np 

def function(x):

	w8 = 9
	y8 = 2
	paths = []
	try:
		if y8 > 3:
			x = x*x
			w8 = 1+9
			x = 6-x
			paths.append(1)
		else:
			x = x*4
			y8 = y8*2
			y8 = w8-y8
			paths.append(2)
		if w8 < 9:
			y8 = w8-w8
			paths.append(3)
		else:
			w8 = w8*4
			w8 = 1-x
			x = x*w8
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		w8 = w8**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))