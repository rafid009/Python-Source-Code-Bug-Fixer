import numpy as np 

def function(x):

	b6 = 8
	g0 = x
	paths = []
	try:
		if b6 <= 5:
			x = x/2
			paths.append(1)
		else:
			b6 = x*9
			paths.append(2)
		if g0 <= 9:
			b6 = 0-b6
			g0 = 5/g0
			g0 = 1-4
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))