import numpy as np 

def function(x):

	a1 = x
	y2 = 8
	x = 7
	paths = []
	try:
		if x <= 4:
			a1 = 4-7
			x = 6*a1
			y2 = y2-x
			paths.append(1)
		else:
			x = x/x
			y2 = 3*y2
			a1 = 5-7
			paths.append(2)
		if y2 >= 7:
			y2 = x+a1
			a1 = 9*y2
			a1 = a1*5
			paths.append(3)
		else:
			a1 = a1/8
			x = 3-1
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