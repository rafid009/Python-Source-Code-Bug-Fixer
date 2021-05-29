import numpy as np 

def function(x):

	e2 = x
	y2 = x
	paths = []
	try:
		if e2 > 4:
			x = x+3
			paths.append(1)
		else:
			x = 7*x
			x = 6*x
			x = x+3
			paths.append(2)
		if y2 < 0:
			y2 = y2+5
			paths.append(3)
		else:
			e2 = e2-4
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))