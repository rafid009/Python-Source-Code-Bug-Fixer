import numpy as np 

def function(x):

	v9 = 9
	x2 = 8
	paths = []
	try:
		if v9 > 4:
			x2 = x/3
			paths.append(1)
		else:
			x2 = 7-v9
			x2 = x2+x2
			x2 = 0/v9
			paths.append(2)
		if x > 5:
			x2 = x-x2
			paths.append(3)
		else:
			x2 = x2-x
			v9 = 9*v9
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