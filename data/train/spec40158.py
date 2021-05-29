import numpy as np 

def function(x):

	i6 = x
	g0 = x
	paths = []
	try:
		if g0 < 1:
			i6 = x+2
			x = 0+3
			g0 = i6/7
			paths.append(1)
		else:
			i6 = 3-7
			paths.append(2)
		if x <= 4:
			x = 5*g0
			g0 = x+g0
			x = x-3
			paths.append(3)
		else:
			i6 = g0-i6
			x = x/6
			g0 = g0+i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))