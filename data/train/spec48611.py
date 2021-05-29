import numpy as np 

def function(x):

	g8 = x
	f5 = 8
	paths = []
	try:
		if f5 < 7:
			f5 = f5+5
			f5 = f5+5
			paths.append(1)
		else:
			g8 = g8-3
			x = g8-x
			paths.append(2)
		if x <= 7:
			x = 6-4
			x = 5-x
			f5 = g8*4
			paths.append(3)
		else:
			g8 = g8/6
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))