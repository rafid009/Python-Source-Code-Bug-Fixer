import numpy as np 

def function(x):

	g0 = x
	b6 = 5
	paths = []
	try:
		if g0 < 9:
			b6 = b6-7
			paths.append(1)
		else:
			x = 7*x
			b6 = g0*6
			g0 = g0*g0
			paths.append(2)
		if b6 > 5:
			b6 = b6+x
			paths.append(3)
		else:
			b6 = 0*1
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))