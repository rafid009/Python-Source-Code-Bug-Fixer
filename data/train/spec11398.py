import numpy as np 

def function(x):

	y3 = 7
	y2 = 2
	paths = []
	try:
		if x > 7:
			y3 = y3-9
			y3 = y2*y3
			y3 = y2-7
			paths.append(1)
		else:
			y2 = y2-0
			y3 = 0*x
			paths.append(2)
		if y2 < 6:
			x = 4*x
			y2 = y2+y2
			paths.append(3)
		else:
			x = x/y3
			y2 = y2/7
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y2 = y3**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))