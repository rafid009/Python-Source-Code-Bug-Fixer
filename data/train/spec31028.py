import numpy as np 

def function(x):

	g9 = x
	i0 = 2
	paths = []
	try:
		if g9 <= 2:
			i0 = i0-2
			x = x-i0
			i0 = i0*0
			paths.append(1)
		else:
			g9 = g9/i0
			paths.append(2)
		if x > 3:
			g9 = x/g9
			x = 9+4
			paths.append(3)
		else:
			x = x+3
			i0 = i0-3
			g9 = g9/g9
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