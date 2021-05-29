import numpy as np 

def function(x):

	g0 = x
	r8 = 0
	paths = []
	try:
		if r8 > 0:
			g0 = x-6
			paths.append(1)
		else:
			g0 = g0*7
			paths.append(2)
		if x <= 2:
			r8 = 6+9
			g0 = g0-g0
			paths.append(3)
		else:
			r8 = r8-g0
			g0 = g0-7
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))