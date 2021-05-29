import numpy as np 

def function(x):

	y2 = x
	q4 = 9
	paths = []
	try:
		if q4 > 6:
			q4 = q4-8
			paths.append(1)
		else:
			y2 = y2+9
			paths.append(2)
		if x < 8:
			x = x*q4
			y2 = y2-x
			q4 = q4-8
			paths.append(3)
		else:
			y2 = 7-y2
			q4 = q4+0
			q4 = q4-2
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