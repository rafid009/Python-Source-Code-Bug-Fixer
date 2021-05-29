import numpy as np 

def function(x):

	k7 = x
	e8 = 2
	paths = []
	try:
		if x >= 2:
			k7 = k7+3
			x = 6*x
			k7 = k7*e8
			paths.append(1)
		else:
			e8 = x+3
			paths.append(2)
		if x >= 9:
			x = x*1
			k7 = 6*e8
			paths.append(3)
		else:
			e8 = 1+e8
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		e8 = k7**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))