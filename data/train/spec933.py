import numpy as np 

def function(x):

	t8 = 5
	a3 = x
	paths = []
	try:
		if a3 < 5:
			t8 = 0+7
			paths.append(1)
		else:
			a3 = 9-1
			paths.append(2)
		if x < 9:
			a3 = 8*a3
			a3 = a3+1
			paths.append(3)
		else:
			a3 = a3/3
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