import numpy as np 

def function(x):

	w0 = 1
	p4 = 9
	paths = []
	try:
		if w0 > 1:
			x = x/6
			paths.append(1)
		else:
			w0 = 5-x
			x = 8-x
			paths.append(2)
		if p4 <= 8:
			x = 1-x
			p4 = 3-7
			p4 = 1/p4
			paths.append(3)
		else:
			x = 3+1
			x = 9-w0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))