import numpy as np 

def function(x):

	w0 = x
	v5 = 9
	x = x
	paths = []
	try:
		if w0 > 2:
			w0 = w0+7
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if w0 > 7:
			w0 = w0-6
			x = v5*x
			x = x*3
			paths.append(3)
		else:
			w0 = w0/x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		v5 = w0**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))