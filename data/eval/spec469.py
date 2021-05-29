import numpy as np 

def function(x):

	r7 = 5
	w0 = 3
	paths = []
	try:
		if w0 > 0:
			r7 = r7/w0
			paths.append(1)
		else:
			w0 = r7+w0
			x = x+x
			paths.append(2)
		if w0 >= 0:
			r7 = 6+0
			x = x-r7
			paths.append(3)
		else:
			r7 = r7+4
			r7 = 1*r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))