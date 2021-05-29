import numpy as np 

def function(x):

	f8 = x
	g4 = x
	paths = []
	try:
		if f8 < 8:
			g4 = x-4
			g4 = g4*1
			paths.append(1)
		else:
			g4 = g4/8
			g4 = 5-1
			paths.append(2)
		if f8 >= 6:
			g4 = 1-f8
			g4 = 1*g4
			paths.append(3)
		else:
			f8 = 1+f8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))