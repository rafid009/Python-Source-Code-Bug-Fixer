import numpy as np 

def function(x):

	g8 = x
	w0 = 7
	paths = []
	try:
		if x <= 5:
			g8 = 6/6
			g8 = g8-1
			w0 = w0*x
			paths.append(1)
		else:
			g8 = 2*g8
			w0 = 5+g8
			x = 8+1
			paths.append(2)
		if x >= 7:
			g8 = g8*0
			paths.append(3)
		else:
			g8 = x*4
			x = 8*5
			g8 = 4*x
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