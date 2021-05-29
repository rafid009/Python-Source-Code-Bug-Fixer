import numpy as np 

def function(x):

	o9 = x
	g0 = x
	x = 4
	paths = []
	try:
		if o9 <= 2:
			o9 = o9/9
			x = x-6
			paths.append(1)
		else:
			o9 = 7*6
			paths.append(2)
		if o9 > 2:
			x = x*1
			x = 7-5
			x = g0+x
			paths.append(3)
		else:
			x = x-8
			o9 = o9+1
			g0 = g0/g0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))