import numpy as np 

def function(x):

	w0 = x
	b4 = x
	paths = []
	try:
		if x < 5:
			b4 = 6*b4
			paths.append(1)
		else:
			b4 = 3/b4
			paths.append(2)
		if x > 4:
			x = x-w0
			w0 = w0+9
			paths.append(3)
		else:
			x = x-1
			b4 = 6-b4
			x = x-x
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