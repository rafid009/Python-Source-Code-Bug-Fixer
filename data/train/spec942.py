import numpy as np 

def function(x):

	q5 = x
	g9 = 5
	paths = []
	try:
		if x >= 6:
			g9 = 6*x
			paths.append(1)
		else:
			g9 = 4/5
			q5 = 4+x
			x = x*8
			paths.append(2)
		if q5 > 0:
			x = g9*1
			g9 = g9*q5
			x = 3*x
			paths.append(3)
		else:
			g9 = g9/x
			g9 = 1+q5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))