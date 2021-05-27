import numpy as np 

def function(x):

	e3 = 4
	v7 = 5
	paths = []
	try:
		if x < 9:
			e3 = x-4
			v7 = 8*7
			paths.append(1)
		else:
			v7 = v7-v7
			paths.append(2)
		if e3 < 4:
			e3 = 4-e3
			paths.append(3)
		else:
			x = 4*e3
			v7 = e3-v7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))