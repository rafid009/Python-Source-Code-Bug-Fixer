import numpy as np 

def function(x):

	b3 = x
	w0 = x
	x = x
	paths = []
	try:
		if x >= 3:
			w0 = w0/1
			b3 = 6*b3
			paths.append(1)
		else:
			b3 = 4+b3
			x = x/8
			paths.append(2)
		if w0 <= 8:
			b3 = 6+0
			paths.append(3)
		else:
			x = x-x
			b3 = w0/3
			x = x/5
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