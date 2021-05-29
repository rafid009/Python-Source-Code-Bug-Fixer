import numpy as np 

def function(x):

	r3 = x
	g0 = 1
	paths = []
	try:
		if x > 2:
			x = x*7
			g0 = g0-g0
			r3 = 8*2
			paths.append(1)
		else:
			x = 7+x
			x = 3+x
			paths.append(2)
		if r3 < 8:
			g0 = x+6
			g0 = g0*7
			r3 = r3/4
			paths.append(3)
		else:
			r3 = r3/7
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))