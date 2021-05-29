import numpy as np 

def function(x):

	y3 = x
	e5 = 8
	paths = []
	try:
		if x < 2:
			y3 = 0*5
			x = x+9
			paths.append(1)
		else:
			e5 = 3*x
			e5 = x*e5
			x = x/y3
			paths.append(2)
		if e5 <= 2:
			y3 = 6/e5
			x = 7-x
			paths.append(3)
		else:
			e5 = e5/1
			e5 = e5-7
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))