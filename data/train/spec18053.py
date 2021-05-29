import numpy as np 

def function(x):

	q6 = x
	g0 = 8
	paths = []
	try:
		if q6 >= 9:
			q6 = 0+q6
			x = x+x
			paths.append(1)
		else:
			q6 = q6*x
			g0 = g0+q6
			paths.append(2)
		if q6 < 4:
			q6 = 9/3
			q6 = g0*q6
			x = x*2
			paths.append(3)
		else:
			g0 = q6*7
			x = x-7
			g0 = g0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))