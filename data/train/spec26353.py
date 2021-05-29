import numpy as np 

def function(x):

	w0 = x
	l0 = 2
	x = x
	paths = []
	try:
		if x > 4:
			x = w0/w0
			l0 = l0+0
			l0 = l0*8
			paths.append(1)
		else:
			l0 = w0*l0
			paths.append(2)
		if l0 <= 4:
			l0 = l0+l0
			x = 1/x
			paths.append(3)
		else:
			l0 = l0/w0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))