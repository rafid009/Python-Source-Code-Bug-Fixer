import numpy as np 

def function(x):

	i4 = x
	a7 = x
	paths = []
	try:
		if a7 < 0:
			a7 = a7*a7
			x = 2-x
			paths.append(1)
		else:
			i4 = a7/i4
			x = 1/3
			a7 = 6-a7
			paths.append(2)
		if x > 3:
			i4 = i4-3
			x = i4-x
			x = 1-x
			paths.append(3)
		else:
			x = 8*x
			i4 = 2+7
			a7 = a7*4
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))