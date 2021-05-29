import numpy as np 

def function(x):

	g9 = 2
	f5 = x
	paths = []
	try:
		if f5 >= 8:
			f5 = 4/f5
			x = x*8
			x = x-x
			paths.append(1)
		else:
			f5 = 5+f5
			g9 = 8-g9
			x = 1*x
			paths.append(2)
		if f5 > 7:
			f5 = 6-1
			paths.append(3)
		else:
			f5 = g9*f5
			x = f5/8
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