import numpy as np 

def function(x):

	g8 = x
	f6 = x
	paths = []
	try:
		if g8 > 7:
			g8 = f6-1
			x = x/6
			f6 = f6+g8
			paths.append(1)
		else:
			x = 6-8
			f6 = 5+f6
			f6 = 3/f6
			paths.append(2)
		if g8 <= 6:
			g8 = g8*g8
			paths.append(3)
		else:
			g8 = g8/8
			g8 = g8*6
			g8 = g8+f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))