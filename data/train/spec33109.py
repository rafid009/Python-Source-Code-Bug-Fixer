import numpy as np 

def function(x):

	o2 = 1
	w0 = 5
	paths = []
	try:
		if w0 > 3:
			w0 = o2*x
			w0 = 6/o2
			paths.append(1)
		else:
			o2 = x-o2
			w0 = w0-0
			x = w0/9
			paths.append(2)
		if x <= 1:
			x = x/9
			x = x-7
			x = x+x
			paths.append(3)
		else:
			w0 = w0-8
			o2 = o2/x
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