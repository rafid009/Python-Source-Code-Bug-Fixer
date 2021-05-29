import numpy as np 

def function(x):

	y5 = x
	q7 = 6
	paths = []
	try:
		if q7 > 7:
			q7 = 5+q7
			y5 = q7+2
			paths.append(1)
		else:
			q7 = q7/9
			y5 = q7+y5
			paths.append(2)
		if y5 < 8:
			y5 = y5*4
			y5 = 5*y5
			paths.append(3)
		else:
			y5 = y5*9
			x = x+y5
			y5 = 9+0
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