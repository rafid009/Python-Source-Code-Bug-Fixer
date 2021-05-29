import numpy as np 

def function(x):

	g0 = x
	b8 = x
	paths = []
	try:
		if g0 <= 6:
			g0 = g0+g0
			x = 8/1
			g0 = 1-g0
			paths.append(1)
		else:
			b8 = g0+b8
			paths.append(2)
		if b8 >= 5:
			x = x+7
			paths.append(3)
		else:
			g0 = b8-6
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		b8 = g0**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))