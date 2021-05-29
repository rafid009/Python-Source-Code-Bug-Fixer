import numpy as np 

def function(x):

	e4 = x
	y5 = x
	x = x
	paths = []
	try:
		if e4 > 9:
			e4 = e4*9
			y5 = y5/x
			e4 = e4*2
			paths.append(1)
		else:
			x = x+5
			x = x+x
			paths.append(2)
		if e4 <= 5:
			x = 0+x
			x = x-x
			x = 2*e4
			paths.append(3)
		else:
			y5 = 7/x
			e4 = 8+8
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