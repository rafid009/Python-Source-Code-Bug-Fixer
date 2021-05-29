import numpy as np 

def function(x):

	f2 = 5
	g0 = 2
	paths = []
	try:
		if g0 < 6:
			x = x*2
			f2 = 5+x
			x = 9+4
			paths.append(1)
		else:
			x = x/5
			x = 5-x
			paths.append(2)
		if x < 2:
			f2 = 6-f2
			x = x-0
			x = x-g0
			paths.append(3)
		else:
			g0 = 9/f2
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