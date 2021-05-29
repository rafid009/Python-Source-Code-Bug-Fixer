import numpy as np 

def function(x):

	y3 = 8
	e6 = 9
	paths = []
	try:
		if e6 > 6:
			x = x+x
			e6 = 8-e6
			y3 = y3+9
			paths.append(1)
		else:
			x = 9*y3
			y3 = 8-y3
			e6 = 0*e6
			paths.append(2)
		if x < 6:
			e6 = e6/7
			y3 = x*6
			e6 = e6-e6
			paths.append(3)
		else:
			y3 = y3/e6
			e6 = y3+8
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		y3 = e6**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))