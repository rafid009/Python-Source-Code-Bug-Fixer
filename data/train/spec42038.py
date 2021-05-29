import numpy as np 

def function(x):

	g8 = 5
	f5 = 4
	paths = []
	try:
		if x > 1:
			g8 = f5+g8
			x = 1-x
			paths.append(1)
		else:
			g8 = 1-g8
			g8 = g8*9
			x = x*x
			paths.append(2)
		if f5 <= 5:
			g8 = 0*g8
			paths.append(3)
		else:
			f5 = 9/f5
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))