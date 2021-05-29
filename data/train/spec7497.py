import numpy as np 

def function(x):

	v3 = x
	e3 = x
	paths = []
	try:
		if x <= 4:
			x = 6/x
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if x >= 6:
			v3 = 3/7
			e3 = 8-e3
			paths.append(3)
		else:
			e3 = 1/4
			e3 = e3/v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		v3 = v3**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))