import numpy as np 

def function(x):

	f0 = x
	g0 = 2
	paths = []
	try:
		if f0 < 0:
			x = x/8
			x = 8-9
			x = x/9
			paths.append(1)
		else:
			g0 = 6+3
			x = x/f0
			f0 = 4*x
			paths.append(2)
		if f0 < 4:
			f0 = f0+7
			paths.append(3)
		else:
			f0 = 6/g0
			f0 = f0-f0
			f0 = 4-f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		g0 = f0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))