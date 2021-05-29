import numpy as np 

def function(x):

	e0 = x
	w8 = 4
	x = x
	paths = []
	try:
		if w8 >= 8:
			x = 1*0
			x = x/4
			w8 = w8-x
			paths.append(1)
		else:
			w8 = 3*w8
			paths.append(2)
		if w8 < 6:
			x = 0*x
			w8 = w8+x
			w8 = 2/3
			paths.append(3)
		else:
			x = x*w8
			e0 = e0-5
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))