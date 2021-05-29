import numpy as np 

def function(x):

	g0 = 6
	j4 = 8
	paths = []
	try:
		if x <= 7:
			g0 = g0+g0
			paths.append(1)
		else:
			x = x*g0
			j4 = 7+j4
			paths.append(2)
		if g0 > 3:
			j4 = j4+x
			g0 = 6+x
			paths.append(3)
		else:
			g0 = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))