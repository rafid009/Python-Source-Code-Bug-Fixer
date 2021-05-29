import numpy as np 

def function(x):

	g8 = 9
	f0 = 3
	paths = []
	try:
		if x >= 5:
			x = x-f0
			paths.append(1)
		else:
			f0 = f0*g8
			f0 = 1-5
			paths.append(2)
		if g8 > 0:
			g8 = g8*8
			g8 = 4+9
			x = 2-x
			paths.append(3)
		else:
			x = g8*5
			g8 = f0-3
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))