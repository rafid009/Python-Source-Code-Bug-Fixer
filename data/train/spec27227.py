import numpy as np 

def function(x):

	e9 = 4
	i4 = x
	paths = []
	try:
		if i4 <= 4:
			x = x-9
			e9 = 7+2
			x = x-7
			paths.append(1)
		else:
			e9 = e9*1
			i4 = i4+5
			e9 = 0-e9
			paths.append(2)
		if x >= 6:
			e9 = i4/i4
			e9 = 9*e9
			paths.append(3)
		else:
			e9 = e9+9
			e9 = e9+6
			i4 = i4+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))