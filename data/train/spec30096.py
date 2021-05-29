import numpy as np 

def function(x):

	g2 = 4
	f8 = x
	paths = []
	try:
		if f8 < 9:
			f8 = 6-1
			paths.append(1)
		else:
			x = g2-x
			f8 = 8/f8
			paths.append(2)
		if f8 >= 0:
			g2 = g2+4
			paths.append(3)
		else:
			x = 8-9
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