import numpy as np 

def function(x):

	w0 = 1
	o1 = x
	x = 2
	paths = []
	try:
		if o1 > 7:
			x = x/2
			w0 = o1-6
			paths.append(1)
		else:
			x = w0+7
			x = 8+6
			paths.append(2)
		if x < 0:
			o1 = 2-o1
			paths.append(3)
		else:
			w0 = 4+w0
			w0 = o1/x
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		x = w0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))