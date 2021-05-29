import numpy as np 

def function(x):

	e6 = 7
	g6 = 3
	x = 0
	paths = []
	try:
		if g6 > 3:
			g6 = g6*g6
			g6 = g6*1
			g6 = g6*x
			paths.append(1)
		else:
			e6 = e6*x
			e6 = e6+8
			paths.append(2)
		if e6 <= 7:
			x = 5+x
			x = x/g6
			e6 = e6-g6
			paths.append(3)
		else:
			e6 = x-7
			x = x-2
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))