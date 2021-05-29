import numpy as np 

def function(x):

	e4 = 6
	v5 = 6
	paths = []
	try:
		if x < 7:
			v5 = 7/9
			paths.append(1)
		else:
			v5 = 4-4
			e4 = e4/e4
			v5 = 6-7
			paths.append(2)
		if v5 <= 0:
			x = e4-9
			e4 = 7/1
			paths.append(3)
		else:
			v5 = 5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))