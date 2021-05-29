import numpy as np 

def function(x):

	f7 = x
	g8 = 9
	paths = []
	try:
		if f7 > 2:
			x = 0+x
			paths.append(1)
		else:
			g8 = g8*f7
			paths.append(2)
		if f7 >= 6:
			f7 = f7*7
			f7 = f7-9
			x = 6*x
			paths.append(3)
		else:
			g8 = g8+8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		f7 = g8**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))