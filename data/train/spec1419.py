import numpy as np 

def function(x):

	y2 = 3
	q0 = x
	paths = []
	try:
		if q0 > 5:
			y2 = y2-y2
			q0 = x-1
			q0 = 9+3
			paths.append(1)
		else:
			y2 = 3*y2
			y2 = 4+y2
			q0 = q0/5
			paths.append(2)
		if x < 4:
			y2 = 6*q0
			paths.append(3)
		else:
			x = y2+x
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