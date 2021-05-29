import numpy as np 

def function(x):

	y3 = x
	v5 = x
	paths = []
	try:
		if y3 > 2:
			v5 = 9*v5
			paths.append(1)
		else:
			y3 = y3/7
			v5 = 8*y3
			paths.append(2)
		if y3 >= 8:
			y3 = y3+4
			paths.append(3)
		else:
			y3 = 6+y3
			y3 = 4/y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		v5 = y3**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))