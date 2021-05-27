import numpy as np 

def function(x):

	g1 = 6
	j4 = 0
	x = x
	paths = []
	try:
		if g1 > 9:
			j4 = j4/3
			g1 = g1*j4
			x = x+x
			paths.append(1)
		else:
			g1 = 1*j4
			j4 = 8-8
			paths.append(2)
		if x > 5:
			x = 4*1
			g1 = g1/3
			paths.append(3)
		else:
			j4 = 5-9
			g1 = g1*x
			x = x-9
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))