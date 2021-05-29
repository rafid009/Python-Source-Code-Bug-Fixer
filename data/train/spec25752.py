import numpy as np 

def function(x):

	r2 = x
	v5 = 7
	x = x
	paths = []
	try:
		if v5 <= 9:
			v5 = v5/3
			v5 = 7+v5
			paths.append(1)
		else:
			r2 = 3+v5
			paths.append(2)
		if x < 7:
			v5 = 2/v5
			r2 = 5-r2
			paths.append(3)
		else:
			v5 = 7-r2
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