import numpy as np 

def function(x):

	q0 = x
	y2 = x
	paths = []
	try:
		if y2 > 1:
			x = x/x
			y2 = 3*y2
			paths.append(1)
		else:
			y2 = y2+6
			paths.append(2)
		if q0 >= 9:
			y2 = 9-y2
			q0 = 1+q0
			q0 = q0*2
			paths.append(3)
		else:
			q0 = 0*3
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))