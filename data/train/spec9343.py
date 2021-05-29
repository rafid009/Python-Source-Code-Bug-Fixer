import numpy as np 

def function(x):

	g0 = x
	q2 = x
	paths = []
	try:
		if g0 < 4:
			g0 = g0/q2
			x = x-9
			g0 = g0*1
			paths.append(1)
		else:
			g0 = 8+q2
			paths.append(2)
		if x > 2:
			x = 3-4
			paths.append(3)
		else:
			q2 = 4/q2
			q2 = q2-g0
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		g0 = q2**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))