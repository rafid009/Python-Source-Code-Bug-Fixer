import numpy as np 

def function(x):

	a1 = x
	y6 = 3
	paths = []
	try:
		if x > 7:
			a1 = y6/6
			y6 = 4+2
			y6 = y6*5
			paths.append(1)
		else:
			y6 = y6/8
			y6 = 9+1
			y6 = 1/4
			paths.append(2)
		if y6 >= 3:
			y6 = 5-y6
			a1 = 7/2
			paths.append(3)
		else:
			a1 = 8*a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))