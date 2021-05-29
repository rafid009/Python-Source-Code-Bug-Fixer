import numpy as np 

def function(x):

	j0 = x
	y3 = 7
	paths = []
	try:
		if x > 9:
			j0 = y3-j0
			y3 = 7-1
			paths.append(1)
		else:
			j0 = j0/x
			j0 = 6/y3
			j0 = j0/j0
			paths.append(2)
		if x > 8:
			x = x*5
			paths.append(3)
		else:
			x = j0+y3
			y3 = x+8
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		y3 = j0**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))