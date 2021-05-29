import numpy as np 

def function(x):

	e3 = 0
	a6 = x
	paths = []
	try:
		if x >= 2:
			e3 = 4*5
			paths.append(1)
		else:
			a6 = a6+3
			paths.append(2)
		if a6 > 9:
			e3 = e3*e3
			e3 = e3*1
			e3 = 6-a6
			paths.append(3)
		else:
			e3 = 8/7
			e3 = 8/e3
			e3 = 5-x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))