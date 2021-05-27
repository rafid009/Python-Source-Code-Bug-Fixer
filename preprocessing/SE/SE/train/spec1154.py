import numpy as np 

def function(x):

	f0 = 7
	g9 = 7
	paths = []
	try:
		if f0 <= 0:
			f0 = 5/f0
			f0 = f0+5
			g9 = f0*g9
			paths.append(1)
		else:
			f0 = f0+g9
			paths.append(2)
		if x > 4:
			x = 1/x
			paths.append(3)
		else:
			f0 = f0+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))