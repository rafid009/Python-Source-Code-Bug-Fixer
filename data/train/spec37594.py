import numpy as np 

def function(x):

	g8 = x
	r2 = x
	paths = []
	try:
		if x < 7:
			g8 = 8/g8
			g8 = r2-3
			g8 = g8*g8
			paths.append(1)
		else:
			g8 = 1-5
			r2 = g8*r2
			g8 = x/g8
			paths.append(2)
		if x > 0:
			x = x+x
			r2 = r2*g8
			g8 = g8-6
			paths.append(3)
		else:
			g8 = g8/9
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))