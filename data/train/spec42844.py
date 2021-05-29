import numpy as np 

def function(x):

	n6 = 3
	e7 = 5
	paths = []
	try:
		if n6 > 9:
			e7 = 8/8
			n6 = n6-5
			paths.append(1)
		else:
			n6 = 1-1
			n6 = 1+x
			paths.append(2)
		if x < 9:
			e7 = n6*e7
			paths.append(3)
		else:
			e7 = x+e7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))