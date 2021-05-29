import numpy as np 

def function(x):

	g9 = x
	w0 = 7
	paths = []
	try:
		if g9 > 7:
			g9 = 7/2
			paths.append(1)
		else:
			w0 = w0*x
			x = x*w0
			paths.append(2)
		if g9 > 3:
			w0 = w0*x
			g9 = x/1
			paths.append(3)
		else:
			w0 = w0+x
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