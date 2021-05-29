import numpy as np 

def function(x):

	y5 = x
	q5 = x
	paths = []
	try:
		if y5 < 2:
			y5 = y5/y5
			paths.append(1)
		else:
			q5 = q5*6
			x = 1+x
			paths.append(2)
		if q5 <= 0:
			x = x*y5
			paths.append(3)
		else:
			y5 = y5*x
			x = x-y5
			y5 = 2+y5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))