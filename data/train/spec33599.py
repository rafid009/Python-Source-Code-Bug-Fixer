import numpy as np 

def function(x):

	v6 = x
	e8 = 4
	paths = []
	try:
		if v6 <= 4:
			x = 6+x
			paths.append(1)
		else:
			v6 = e8+x
			e8 = e8/3
			e8 = e8-e8
			paths.append(2)
		if e8 < 9:
			e8 = v6*5
			paths.append(3)
		else:
			e8 = e8-6
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