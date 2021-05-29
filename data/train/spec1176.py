import numpy as np 

def function(x):

	q2 = 3
	g1 = 6
	paths = []
	try:
		if q2 <= 7:
			q2 = q2+4
			paths.append(1)
		else:
			g1 = 3/7
			paths.append(2)
		if g1 <= 0:
			q2 = q2*1
			x = 8+x
			g1 = g1+5
			paths.append(3)
		else:
			q2 = q2-8
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		g1 = q2**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))