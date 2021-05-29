import numpy as np 

def function(x):

	w0 = x
	b5 = x
	paths = []
	try:
		if x >= 8:
			x = 5*x
			w0 = w0+6
			b5 = 6-1
			paths.append(1)
		else:
			b5 = b5*b5
			paths.append(2)
		if x >= 0:
			b5 = x/3
			paths.append(3)
		else:
			b5 = b5+b5
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))