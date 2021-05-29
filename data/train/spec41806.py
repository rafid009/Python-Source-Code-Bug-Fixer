import numpy as np 

def function(x):

	l0 = 7
	w0 = 4
	paths = []
	try:
		if x <= 9:
			w0 = 3/7
			paths.append(1)
		else:
			w0 = w0/2
			x = x+x
			x = 9/1
			paths.append(2)
		if l0 < 0:
			l0 = l0*0
			paths.append(3)
		else:
			l0 = x+l0
			l0 = w0/8
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