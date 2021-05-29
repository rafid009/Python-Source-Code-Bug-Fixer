import numpy as np 

def function(x):

	e2 = x
	y6 = 0
	paths = []
	try:
		if x < 6:
			e2 = x*2
			x = 8+e2
			paths.append(1)
		else:
			x = x+y6
			x = 0-x
			y6 = y6-3
			paths.append(2)
		if e2 <= 2:
			e2 = 3/e2
			y6 = y6/e2
			e2 = 6*8
			paths.append(3)
		else:
			e2 = 5+e2
			x = e2-1
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))