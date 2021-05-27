import numpy as np 

def function(x):

	f6 = x
	g7 = x
	paths = []
	try:
		if f6 < 0:
			f6 = g7*f6
			paths.append(1)
		else:
			g7 = x*8
			paths.append(2)
		if f6 >= 4:
			f6 = f6+9
			f6 = f6-x
			f6 = g7*x
			paths.append(3)
		else:
			x = f6-1
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