import numpy as np 

def function(x):

	r7 = x
	g9 = x
	paths = []
	try:
		if g9 >= 1:
			r7 = 3/r7
			r7 = r7+r7
			paths.append(1)
		else:
			r7 = r7+8
			x = 7-x
			paths.append(2)
		if r7 < 9:
			r7 = g9*8
			r7 = g9+0
			x = 3-9
			paths.append(3)
		else:
			x = x+r7
			x = 9+x
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